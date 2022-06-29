from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
#import requests
from core.carrito import Carrito
from core.models import Producto
#r = requests.get('http://127.0.0.1:8000/api/categorias/')



# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    
#def categorias(request):
    #response = requests.get('http://127.0.0.1:8000/api/categorias/')
    #categorias = response.json()
    #print(categorias)

    #return render(request, "core/categorias.html", {'categorias':categorias})
    #pass 

def tienda(request):
    #return HttpResponse("Hola")
    productos = Producto.objects.all()
    return render(request, "tienda.html" , {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def pago(request):
    return render(request, "pago.html")
