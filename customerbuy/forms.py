from django import forms
from .models import CustomerBuy

class CustomerBuyForm(forms.ModelForm):
	
	class Meta:
		model = CustomerBuy
		fields = ['customer','ruc','logo','foto_institucional','razon_social','phone' ,'cel' ,'inicio_de_actividades','numero_de_trabajadores','website','email' ,'sector', ]
