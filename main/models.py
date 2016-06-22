from django.db import models

# Create your models here.


class producto(models.Model):
	producto = models.CharField(max_length=40)
	precio = models.IntegerField(max_length=11, blank = True, null=True )
	descripcion = models.TextField(blank=True, null = True)

	def __unicode__( self ):
		return '%s: %s'%( self.producto, self.descripcion) 
	
	class Meta:
		verbose_name_plural = "productos"



class cliente(models.Model):
	nombres = models.CharField(max_length=80)
	documento = models.IntegerField(max_length=11, blank = True, null=True )
	detalles = models.TextField(blank=True, null = True)

	def __unicode__( self ):
		return '%s: %s'%( self.nombres, self.documento)
	
	class Meta:
		verbose_name_plural = "clientes"


class sede(models.Model):
	sede = models.CharField(max_length=40)
	direccion =  models.CharField(max_length=40)

	def __unicode__( self ):
		return '%s'%( self.sede)    
	
	class Meta:
		verbose_name_plural = "sedes"


	
class compra(models.Model):
	id_cliente = models.ForeignKey('main.cliente')
	id_producto = models.ForeignKey('main.producto')
	id_sede = models.ForeignKey('main.sede', null=True, blank = True)

	precio = models.IntegerField(max_length=11, blank = True, null=True )
	descripcion = models.TextField(blank=True, null = True)
	fecha = models.DateField(auto_now = True)

	def __unicode__( self ):
		return '%s: %s - %s'%( self.id, self.descripcion, self.precio)
	
	class Meta:
		verbose_name_plural = "compras"



class log(models.Model):
	fecha = models.DateField(auto_now = True)
	descripcion = models.TextField(blank=True, null = True)
    
	def __unicode__( self ):
		return '%s: %s'%( self.fecha, self.descripcion)

	class Meta:
		verbose_name_plural = "logs"

