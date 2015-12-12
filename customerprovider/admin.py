from django.contrib import admin

from .models import *

admin.site.register(CustomerProvider)
admin.site.register(TagProductCustomerProvider)
admin.site.register(ProductCustomerProvider)
admin.site.register(AddressCustomerProvider)
admin.site.register(ContactCustomerProvider)
