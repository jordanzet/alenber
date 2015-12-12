from django import forms
from .models import CustomerProvider


class CustomerProviderForm(forms.ModelForm):
	
	class Meta:
		model = CustomerProvider
		fields = ['ruc','logo','foto_institucional','razon_social','phone' ,'cel' ,'inicio_de_actividades','numero_de_trabajadores','website','email' ,'sector', ]


