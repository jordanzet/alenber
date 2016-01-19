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
from users.forms import UserCreationEmailForm, EmailAuthenticationForm, UserCreationAdminForm
from .forms import *

def index(request):
	""" pagina informativa de marketing y publicidad de un cliente comprador"""
	usuario = request.user
	template = 'customerbuy/index.html'
	return render_to_response(template,{'usuario': usuario},context_instance=RequestContext(request))

def signup(request):
	"""registro basico del cliente comprador"""
	form = UserCreationEmailForm(request.POST or None)
	if form.is_valid():
		comp = form.save()
		comp.groups.add(Group.objects.get(name='comprador'))
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active: login(request, user)

		return HttpResponseRedirect("/comprador/registro/paso1")

	# crear el user profile
	# redireccionar al home
	template = 'customerbuy/signup.html'
	return render(request, template,{'form':form})
	#return render_to_response("customer/signup.html", {'form': form,}, context_instance=RequestContext(request))

def step1(request):
	""" Paso 1 del registro de perfil """
	if request.method == 'POST':
		form = CustomerBuyForm(request.POST)
		if form.is_valid():
			cust = form.save(commit=False)
			cust.customer = request.user
			cust.save()
			return HttpResponseRedirect("/comprador/")
	else:
		form = CustomerBuyForm()
	template = 'customerbuy/step1.html'
	return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))

def step2(request):
	"""registro de usuario administrador, del cliente comprador"""
	form = UserCreationAdminForm(request.POST or None)
	if form.is_valid():
		comp = form.save()
		comp.groups.add(Group.objects.get(name='usuario-admin-compras'))

		return HttpResponseRedirect("/comprador/paso3/")

	# crear el user profile
	# redireccionar al home
	template = 'customerbuy/step2.html'
	return render(request, template,{'form':form})
	#return render_to_response("customer/signup.html", {'form': form,}, context_instance=RequestContext(request))

def step3(request):
	""" Paso 1 del registro de perfil """
	if request.method == 'POST':
		form = CustomerBuyForm(request.POST)
		if form.is_valid():
			cust = form.save(commit=False)
			cust.customer = request.user
			cust.save()
			return HttpResponseRedirect("/comprador/")
	else:
		form = CustomerBuyForm()
	template = 'customerbuy/step3.html'
	return render_to_response(template,context_instance=RequestContext(request,{'form': form} ))

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




def register_tag_product_customer_buy(request):
	form = TagProductCustomerBuyForm(request.POST)
	if form.is_valid():
		ls = form.save(commit=False)
		ls.customer_buy__customer = request.user
		ls.save()

	template = 'customerbuy/register_tag_product_customer_buy.html'
	return render(request, template ,{'form':form})
