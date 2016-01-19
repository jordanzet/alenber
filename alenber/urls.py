from django.conf.urls import include, url
from django.contrib import admin

from home import views
from home import urls as home_urls

#from customer import urls as customer_urls

from users import urls as users_urls
from customerbuy import urls as customerbuy_urls
from customerprovider import urls as customerprovider_urls

from django.conf import settings
urlpatterns = [
	# Examples:
	# url(r'^$', 'alenber.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	#url('^', include('django.contrib.auth.urls')),
	url(r'^$', views.home, name='home'),
	url(r'^', include(home_urls)),
	#url(r'^', include(customer_urls)),
	url(r'^', include(users_urls, namespace='users')),
	url(r'^comprador/', include(customerbuy_urls, namespace='buy')),
	url(r'^proveedor/', include(customerprovider_urls, namespace='provider')),
	#url(r'^', include(customer_urls, namespace="customer")),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
]
