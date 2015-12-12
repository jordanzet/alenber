# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from .forms import EmailAuthenticationForm

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User, Group
#from django.views.generic.edit import FormView


def login_user(request):
	form=EmailAuthenticationForm(request.POST or None)
	if form.is_valid():
		login(request,form.get_user())

	# redireccionar al home

	return render(request,'customer/sigin.html',{'form':form}) 

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/iniciar-sesion/')