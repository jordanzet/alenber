from django import forms
from .models import CustomerBuy, TagProductCustomerBuy, ProductCustomerBuy, AddressCustomerBuy, ContactCustomerBuy


class CustomerBuyForm(forms.ModelForm):
	class Meta:
		model = CustomerBuy
		#fields = '__all__'
		exclude = ['customer',]


class TagProductCustomerBuyForm(forms.ModelForm):
	class Meta:
		model = TagProductCustomerBuy
		fields = ['name','customer_buy']


class ProductCustomerBuyForm(forms.ModelForm):
	class Meta:
		model = ProductCustomerBuy
		fields = ['name_product','image_product','customer_buy','tag_product']


class AddressCustomerBuyForm(forms.ModelForm):
	class Meta:
		model = AddressCustomerBuy
		fields = ['title','region', 'provincia','distrito','direccion','customer_buy']


class ContactCustomerBuyForm(forms.ModelForm):
	class Meta:
		model = ContactCustomerBuy
		fields = ['title','telefono','email','customer_buy']
	

