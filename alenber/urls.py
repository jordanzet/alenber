from django.conf.urls import include, url
from django.contrib import admin

from home import views
from home import urls as home_urls

#from customer import urls as customer_urls

from customerbuy import urls as customerbuy_urls
from customerprovider import urls as customerprovider_urls

urlpatterns = [
	# Examples:
	# url(r'^$', 'alenber.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	#url('^', include('django.contrib.auth.urls')),
	url(r'^$', views.home, name='home'),
	url(r'^', include(home_urls)),
	#url(r'^', include(customer_urls)),
	url(r'^comprador/', include(customerbuy_urls, namespace='customer-buy')),
	url(r'^proveedor/', include(customerprovider_urls, namespace='customer-provider')),
	#url(r'^', include(customer_urls, namespace="customer")),
]
