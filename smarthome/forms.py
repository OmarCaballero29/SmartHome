from django import forms
from django.forms import fields
from .models import Inmueble, Images
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput(attrs={'class': 'form-control','autocomplete':'off'}))
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'type':'email', 'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre(s)',widget=forms.TextInput(attrs={'class': 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class': 'form-control','autocomplete':'off'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'off'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'off'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        help_texts = {k:"" for k in fields}