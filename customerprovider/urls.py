from django.conf.urls import patterns, include, url
from customerprovider import views
#|from .views import RegisterView

urlpatterns = [
	url(r'^proveedor/$','customer.views.customer_provider',name='customer_provider'),
	url(r'^proveedor/registro/','customer.views.signup_customer_provider',name='signup_customer_provider'),
	url(r'^proveedor/editar-perfil/','customer.views.edit_profile_provider',name='edit_profile_provider'),
	#url(r'^p/(?P<usuario>[-\w]+)/$',views.profile_customer_buy, name='profile_customer_buy'),
]