from django.conf.urls import patterns, include, url
from . import views
#|from .views import RegisterView

urlpatterns = [
	#url(r'^p/(?P<usuario>[-\w]+)/$',views.profile_customer_buy, name='profile_customer_buy'),

	url(r'^$',views.index,name='index'),
	url(r'^registro/$',views.signup,name='signup'),
	url(r'^registro/paso1/$',views.step1,name='step1'),
	url(r'^registro/paso2/$',views.step2,name='step2'),
	url(r'^registro/paso3/$',views.step3,name='step3'),
	#url(r'^registro/paso4',views.step4,name='step4'),

	#url(r'^editar-perfil/',views.register,name='register_profile_customer_buy'),
	#url(r'salir', views.logout_user, name='logout_user'),
	url(r'^(?P<usuario>[-\w]+)/$',views.profile, name='profile'),
	url(r'^(?P<usuario>[-\w]+)/admin/$',views.admin, name='admin'),
]