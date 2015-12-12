# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, response

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic.edit import FormView


#from .models import CustomerBuy
from users.forms import UserCreationEmailForm

def customer_provider(request):
	""" pagina informativa de marketing y publicidad de un cliente proveedor"""
	usuario = request.user
	return render_to_response('base.html',{'usuario': usuario},context_instance=RequestContext(request))

def signup_customer_provider(request):
	"""registro de cliente proveedor"""

	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		prov = form.save()
		prov.groups.add(Group.objects.get(name='proveedor'))
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active: login(request, user)

		return HttpResponseRedirect("/proveedor/editar-perfil/")

	# loguear el usuario y llevarlo al registro de cliente comprador

	# crear el user profile
	# redireccionar al home
	return render(request,'customer/signup.html',{'form':form})
	#return render_to_response("customer/signup.html", {'form': form,}, context_instance=RequestContext(request))

def edit_profile_provider(request):
	if request.method == 'POST':
		form = CustomerBuyForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = CustomerBuyForm()
	template = 'customer/edit-profile-buy.html'
	return render(request,template,{'form':form})
	#return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))
