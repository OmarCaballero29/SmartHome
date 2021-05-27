from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inmueble/<int:pk>/', views.details , name='details'),
    path('buscar/', views.search, name='search'),
    path('publicacion/crear', views.new_publication, name='new_publication'),
]