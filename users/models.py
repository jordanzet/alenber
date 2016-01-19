from django.db import models



class UsuarioAdminCompras(models.Model):
	cargo = models.CharField(help_text='ingrese su cargo corporativo', max_length=50)

	class Meta:
		verbose_name = "UsuarioAdminCompras"
		verbose_name_plural = "UsuarioAdminComprass"

	def __unicode__(self):
		pass
	

class UsuarioAdminVentas(models.Model):
	cargo = models.CharField(help_text='ingrese su cargo corporativo', max_length=50)

	class Meta:
		verbose_name = "UsuarioAdminCompras"
		verbose_name_plural = "UsuarioAdminComprass"

	def __unicode__(self):
		pass


class UsuarioJefe(models.Model):
	cargo = models.CharField(help_text='ingrese su cargo corporativo', max_length=50)

	class Meta:
		verbose_name = "UsuarioAdminCompras"
		verbose_name_plural = "UsuarioAdminComprass"

	def __unicode__(self):
		pass


class Usuario(models.Model):
	cargo = models.CharField(help_text='ingrese su cargo corporativo', max_length=50)

	class Meta:
		verbose_name = "UsuarioAdminCompras"
		verbose_name_plural = "UsuarioAdminComprass"

	def __unicode__(self):
		pass

