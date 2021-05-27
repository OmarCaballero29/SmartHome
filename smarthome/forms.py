from django import forms
from .models import Inmueble, Images


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label="Imagen")

    class Meta:
        model = Images
        fields = ('image', )

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
                'descripcion'
                )
    
    tipo_inmueble = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ej: \"Casa\", \"Departamento\".','autocomplete':'off'}),label='Tipo de Inmueble')
    tipo_oferta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ej: \"Renta\", \"Venta\".','autocomplete':'off'}),label='Tipo de Oferta')
    precio = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','min':'0','autocomplete':'off'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ej: \"Calle, Número exterior y/o interior, Colonia, Código postal, Ciudad, Estado, Pais\".','autocomplete':'off'}),label='Dirección del Inmueble')
    superficie = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','min':'0','autocomplete':'off'}),label='Superficie en m²')
    habitaciones = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','min':'0','autocomplete':'off'}),label='Número de habitaciones')
    baños = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','min':'0','autocomplete':'off'}),label='Número de baños')
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','autocomplete':'off'}),label='Descripción del inmueble')