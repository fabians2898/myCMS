from django import forms

from .models import *

class ComprasForm(forms.ModelForm):

	class Meta:
		model = compra
		fields = ('id_cliente','id_producto','id_sede','precio','descripcion')


class SedesForm(forms.ModelForm):

	class Meta:
		model = sede
		fields = ('sede','direccion')

class ClientesForm(forms.ModelForm):

	class Meta:
		model = cliente
		fields = ('nombres','documento','detalles')


class ProductosForm(forms.ModelForm):

	class Meta:
		model = producto
		fields = ('producto','precio','descripcion')


		