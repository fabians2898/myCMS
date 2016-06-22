from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from main.models import *
from .forms import *

# Create your views here.

@csrf_exempt
def compras(request):
	if request.method == "POST":
	    form = ComprasForm(request.POST)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.save()
	        return redirect('/')
	else:
		compras = compra.objects.all()
		comprasForm = ComprasForm()
		context = {'compras': compras, 'comprasForm': comprasForm}
	
	return render(request, 'compras.html', context)
		
		
	


@csrf_exempt
def clientes(request):
	if request.method == "POST":
	    form = ClientesForm(request.POST)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.save()
	        return redirect('clientes.html')
	else:
		clientes = cliente.objects.all()
		clientesForm = ClientesForm()
		context = {'clientes': clientes, 'clientesForm': clientesForm}
		
	return render(request, 'clientes.html', context)



@csrf_exempt
def sedes(request):

	if request.method == "POST":
	    form = SedesForm(request.POST)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.save()
	        return redirect('sedes.html')
	else:
		sedes = sede.objects.all()
		sedesForm = SedesForm()
		context = {'sedes': sedes, 'sedesForm': sedesForm}
	
	return render(request, 'sedes.html', context)

	
@csrf_exempt
def productos(request):
   	
   	if request.method == "POST":
	    form = ProductosForm(request.POST)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.save()
	        return redirect('productos.html')
	else:
		productos = producto.objects.all()
		productosForm = ProductosForm()
		context = {'productos': productos, 'productosForm': productosForm}
	
	return render(request, 'productos.html', context)
