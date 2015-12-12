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


from .models import CustomerBuy
from users.forms import UserCreationEmailForm,EmailAuthenticationForm

def customer_buy(request):
	""" pagina informativa de marketing y publicidad de un cliente comprador"""
	usuario = request.user
	return render_to_response('base.html',{'usuario': usuario},context_instance=RequestContext(request))

def signup_customer_buy(request):
	"""registro de cliente comprador"""
	form = UserCreationEmailForm(request.POST or None)
	if form.is_valid():
		comp = form.save()
		comp.groups.add(Group.objects.get(name='comprador'))
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active: login(request, user)

		return HttpResponseRedirect("/comprador/editar-perfil/")

	# crear el user profile
	# redireccionar al home
	return render(request,'customer/signup.html',{'form':form})
	#return render_to_response("customer/signup.html", {'form': form,}, context_instance=RequestContext(request))


def signup_profile_customer_buy(request):
	if request.method == 'POST':
		form = CustomerBuyForm(request.POST)
		if form.is_valid():
			cust = form.save(commit=False)
			cust.customer = request.user
			#form.save(commit=False)
			#customer = request.user__id
			#form.save()
			cust.save()
			return HttpResponseRedirect("/comprador/")
	else:
		form = CustomerBuyForm()
	template = 'customer/edit-profile-buy.html'
	return render(request,template,{'form':form})
	#return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))

def signup_product_customer_buy(request):
	pass


def signup_address_customer_buy(request):
	pass

def signup_contact_customer_buy (request):
	pass

def profile_customer_buy(request,usuario):
	#usuario = request.user
	cus_buy = CustomerBuy.objects.get(customer__username=usuario)
	template = 'xd.html'
	return render(request, template, {'cus_buy':cus_buy})	

