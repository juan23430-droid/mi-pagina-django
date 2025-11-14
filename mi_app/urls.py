from django.urls import path
from . import views

urlpatterns = [
    # Al ir a la URL raíz de la app (ej: http://127.0.0.1:8000/) 
    # se ejecuta la función 'views.inicio'
    path('', views.inicio, name='inicio'), 
]