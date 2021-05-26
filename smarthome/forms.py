from django import forms
from .models import AlbumImagenes, Inmueble


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = AlbumImagenes
        fields = ['album', 'imagen']

class InmuebleForm(forms.ModelForm):

    class Meta:
        model = Inmueble
        fields = ('tipo_inmueble',
                'tipo_oferta',
                'precio',
                'direccion',
                'superficie',
                'habitaciones',
                'baños',
                'descripcion',
                'disponible'
                )