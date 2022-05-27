from django.urls import path
from .views import home, categorias

urlpatterns = [
    path('', home, name="home"),
    path('categorias/', categorias, name='categorias'),

]

