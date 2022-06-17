from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests

r = requests.get('http://127.0.0.1:8000/api/categorias/')



# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    
def categorias(request):
    response = requests.get('http://127.0.0.1:8000/api/categorias/')
    categorias = response.json()
    print(categorias)

    return render(request, "core/categorias.html", {'categorias':categorias})
    pass 


