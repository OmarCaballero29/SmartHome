from django.urls import path
from django.conf import settings
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inmueble/<int:pk>/', views.details , name='details'),
    path('buscar/', views.search, name='search'),
    path('publicacion/crear', views.new_publication, name='new_publication'),
    path('publicacion/<int:pk>/editar/', views.publication_edit, name='publication_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.register, name='register'),
    path('<int:fav_id>/favorito/', views.favorite, name='favorite'),
    path('favoritos/', views.list_favorites, name='favorites'),
    path('contacto/', views.contact, name='contact'),
]