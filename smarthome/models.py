from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Inmueble(models.Model):
    tipo_inmueble = models.CharField(max_length = 50)
    tipo_oferta = models.CharField(max_length = 20)
    propietario = models.ForeignKey(User, default=None, on_delete=models.CASCADE )
    precio = models.IntegerField()
    direccion = models.CharField(max_length = 200)
    superficie = models.IntegerField()
    habitaciones = models.IntegerField()
    baños = models.IntegerField()
    descripcion = models.TextField(blank = True)
    fecha_publicacion = models.DateTimeField(default = timezone.now)
    disponible = models.BooleanField(default = True)
    favorito = models.ManyToManyField(User, related_name="favourite", blank=True)

def get_image_filename(instance, filename):
    id = instance.inmueble.id
    slug = slugify(id)
    return "inmuebles_images/%s-%s" % (slug, filename)  

class Images(models.Model):
    inmueble = models.ForeignKey(Inmueble, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = get_image_filename,
                                verbose_name='Image',default='inmuebles_images/no-img.jpg')
