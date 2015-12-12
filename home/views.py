# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, render
from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, response
from django.template import RequestContext


#from django.contrib import messages
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User, Group
#from django.views.generic.edit import FormView

def home(request):
	#locales = Local.objects.order_by("nombre").all()[:6]
	"""tags = Tag.objects.all()
	cat_locales = CategoryCompany.objects.all()
	distritos = Distrito.objects.all()
	return render(request, 'home/index.html', locals() , content_type="text/html")"""
	cliente = request.user
	return render_to_response('home/index.html',{'cliente':cliente}, context_instance=RequestContext(request))

#def about(request):
#	usuario = request.user
#	return render_to_response('home/about.html',{'usuario': usuario},context_instance=RequestContext(request))
