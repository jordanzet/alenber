from django.conf.urls import include, url
from customerbuy import views
#|from .views import RegisterView

urlpatterns = [
	url(r'$',views.customer_buy,name='customer_buy'),
	url(r'registro/',views.signup_customer_buy,name='signup_customer_buy'),
	#url(r'editar-perfil/',views.edit_profile_buy,name='edit_profile_buy'),
	#url(r'salir', views.logout_user, name='logout_user'),
	#url(r'^c/(?P<usuario>[-\w]+)/$',views.profile_customer_buy, name='profile_customer_buy'),
]
