from django.contrib import admin

from .models import *

class CustomerBuyAdmin(admin.ModelAdmin):
	list_display = ('id','customer','ruc','razon_social','phone','cel', 'inicio_de_actividades', 'numero_de_trabajadores', 'website','email','sector')


admin.site.register(CustomerBuy, CustomerBuyAdmin)
admin.site.register(TagProductCustomerBuy)
admin.site.register(ProductCustomerBuy)
admin.site.register(AddressCustomerBuy)
admin.site.register(ContactCustomerBuy)


