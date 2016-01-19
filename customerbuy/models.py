# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import datetime


class CustomerBuy(models.Model):
	"""Empresa que compra """
	customer = models.OneToOneField(User)
	ruc = models.BigIntegerField(help_text='Ingrese el numero de RUC', verbose_name='RUC de la empresa') #ruc debe tener 12 digitos
	logo = models.ImageField(upload_to='customer_buy_logo/',blank=True)
	foto_institucional = models.ImageField(upload_to='customer_buy_foto_portada/',blank=True)
	razon_social = models.CharField(max_length=150,help_text='ingrese la razon social', verbose_name='Razon Social de la Empresa')
	phone = models.IntegerField(blank=True, help_text='Ingrese su Numero de Telefono', verbose_name='Telefono') # tipo de telefono si es bitel, nextel o claro
	cel = models.IntegerField(blank=True, help_text='Ingrese su Numero de celular', verbose_name='Celular')

	inicio_de_actividades = models.DateField(help_text='Ingrese la fecha de inicio de actividades', verbose_name='Fecha de Inicio de Actividades') #fecha de inicio de la empresa

	NUMERO_DE_TRABAJADORES=(
		('1t','1 trabajador'),
		('2a10t','2 a 10 trabajadores'),
		('11a100t','11 a 100 trabajadores'),
		('101a1000t','101 a 1000 trabajadores'),
		('1001a5000t','1001 a 5000 trabajadores'),
		('5000a+t','5000 a + trabajadores'),

	)
	numero_de_trabajadores = models.CharField(max_length=250, choices=NUMERO_DE_TRABAJADORES, default='1 trabajador') #opciones de un listado
	website = models.URLField(blank=True,help_text='Ingrese su sitio web', verbose_name='Sitio Web')
	email = models.EmailField(blank=True, help_text='ingrese su email', )
	sector = models.CharField(max_length=150, blank=True, help_text='ingrese su sector')

	class Meta:
		verbose_name = "Empresa compradora"
		verbose_name_plural = "Empresas compradoras"

	#def __unicode__(self):
	#	self.razon_social


class TagProductCustomerBuy(models.Model):
	""" categoria de productos de la empresa compradora """
	name = models.CharField(max_length=50)
	customer_buy = models.ForeignKey(CustomerBuy)
	
	class Meta:
		verbose_name = "Categoria de producto de la empresa proveedora"
		verbose_name_plural = "Categorias de los productos de la empresa proveedora"

	def __unicode__(self):
		return self.name


class ProductCustomerBuy(models.Model):
	""" Productos que la empresa comprara"""
	name_product = models.CharField(max_length=250)
	image_product = models.ImageField(upload_to='product_customer_buy/', blank=True)
	customer_buy = models.ForeignKey(CustomerBuy)
	tag_product = models.ForeignKey(TagProductCustomerBuy)

	class Meta:
		verbose_name = "Producto de la empresa compradora"
		verbose_name_plural = "Productos de la empresa compradora"
		
	def __unicode__(self):
		return self.name_product


class AddressCustomerBuy(models.Model):
	""" Dirección de Oficinas y locales de la empresa """
	TITULO_DE_LA_DIRECCION = (
		('OFICINA_PRINCIPAL', 'Oficina Principal'),
		('SUCURSAL', 'Sucursal'),
		('ALMACEN', 'Almacen'),
		('PLANTA', 'Planta'),
	)
	title = models.CharField(max_length=150, choices=TITULO_DE_LA_DIRECCION,default='OFICINA_PRINCIPAL', help_text='Titulo de la Direccion') #oficina principal, almacen, otros
	region = models.CharField(max_length=150,help_text='region')
	provincia = models.CharField(max_length=150,help_text='provincia')
	distrito = models.CharField(max_length=150,help_text='distrito')
	direccion = models.CharField(max_length=150,help_text='Direccion de la Empresa')
	customer_buy = models.ForeignKey(CustomerBuy)

	class Meta:
		verbose_name = "Direccion de la empresa compradora"
		verbose_name_plural = "Direcciones de la empresa compradora"
		
	def __unicode__(self):
		return self.title


class ContactCustomerBuy(models.Model):
	""" datos de contacto para el proveedor """
	title = models.CharField(max_length=50) #lugar_o_area
	telefono = models.IntegerField()
	email = models.EmailField()
	customer_buy = models.ForeignKey(CustomerBuy)
	
	class Meta:
		verbose_name = "Dato de Contacto de la empresa compradora"
		verbose_name_plural = "Datos de Contacto de la empresa compradora"

	def __unicode__(self):
		self.title
