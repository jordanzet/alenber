from django.conf.urls import include, url
from users import views


urlpatterns = [
	url(r'iniciar-sesion/',views.login_user,name='login_user'),
	url(r'salir', views.logout_user, name='logout_user'),
	#url(r'^u/(?P<usuario>[-\w]+)/$',views.profile_user, name='profile_user'),
]