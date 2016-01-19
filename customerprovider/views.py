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
from users.forms import UserCreationEmailForm, UserCreationAdminForm
from .forms import *

def index(request):
	""" pagina informativa de marketing y publicidad de un cliente proveedor"""
	usuario = request.user
	template = 'customerprovider/index.html'
	return render_to_response(template,{'usuario': usuario},context_instance=RequestContext(request))

def signup(request):
	"""registro basico del cliente proveedor"""
	form = UserCreationEmailForm(request.POST or None)
	if form.is_valid():
		prov = form.save()
		prov.groups.add(Group.objects.get(name='proveedor'))
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active: login(request, user)

		return HttpResponseRedirect("/proveedor/registro/paso1")

	# crear el user profile
	# redireccionar al home
	template = 'customerprovider/signup.html'
	return render(request, template,{'form':form})
	#return render_to_response("customer/signup.html", {'form': form,}, context_instance=RequestContext(request))

def step1(request):
	""" Paso 1 del registro de perfil """
	if request.method == 'POST':
		form = CustomerProviderForm(request.POST)
		if form.is_valid():
			cust = form.save(commit=False)
			cust.customer = request.user
			cust.save()
			return HttpResponseRedirect("/proveedor/")
	else:
		form = CustomerProviderForm()
	template = 'customerprovider/step1.html'
	return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))

def step2(request):
	"""registro de usuario administrador, del cliente proveedor"""
	form = UserCreationAdminForm(request.POST or None)
	if form.is_valid():
		comp = form.save()
		comp.groups.add(Group.objects.get(name='usuario-admin-compras'))

		return HttpResponseRedirect("/proveedor/paso3/")

	# crear el user profile
	# redireccionar al home
	template = 'customerprovider/step2.html'
	return render(request, template,{'form':form})
	#return render_to_response("customer/signup.html", {'form': form,}, context_instance=RequestContext(request))

def step3(request):
	""" Paso 1 del registro de perfil """
	if request.method == 'POST':
		form = CustomerProviderForm(request.POST)
		if form.is_valid():
			cust = form.save(commit=False)
			cust.customer = request.user
			cust.save()
			return HttpResponseRedirect("/proveedor/")
	else:
		form = CustomerProviderForm()
	template = 'customerprovider/step3.html'
	return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))



def customer_provider(request):
	""" pagina informativa de marketing y publicidad de un cliente proveedor"""
	usuario = request.user
	template = 'customerprovider/index.html'
	return render_to_response(template,{'usuario': usuario},context_instance=RequestContext(request))

def edit_profile_provider(request):
	if request.method == 'POST':
		form = CustomerProviderForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
	else:
		form = CustomerProviderForm()
	template = 'customer/edit-profile-buy.html'
	return render(request,template,{'form':form})
	#return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))






##############################
##############################

def profile(request,usuario):
	#usuario = request.user
	cus_buy = CustomerBuy.objects.get(customer__username=usuario)
	# = cus_buy.customer

	template = 'customerbuy/profile.html'
	return render(request, template, {'cus_buy':cus_buy})	

def admin(request, usuario):
	cus_buy = CustomerBuy.objects.get(customer__username=usuario)
	template = 'customerbuy/admin/dashboard.html'
	return render(request, template, {'cus_buy':cus_buy})
