from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone 

# Create your models here.
class Inmueble(models.Model):
    tipo_inmueble = models.CharField(max_length = 50)
    tipo_oferta = models.CharField(max_length = 20, blank = True)
    precio = models.IntegerField()
    direccion = models.CharField(max_length = 200)
    superficie = models.IntegerField()
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    descripcion = models.TextField(blank = True)
    fecha_publicacion = models.DateTimeField(default = timezone.now)
    disponible = models.BooleanField(default = True)

class AlbumImagenes(models.Model):
    album = models.ForeignKey(Inmueble, related_name='images', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'smarthome/images/')