# Generated by Django 3.1.7 on 2021-05-25 02:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='tipo',
            new_name='tipo_inmueble',
        ),
        migrations.RemoveField(
            model_name='inmueble',
            name='otras_caracteristicas',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='tipo_oferta',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='smarthome/static/images/no-img.jpg', upload_to='albums/inmuebles/')),
                ('inmueble', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='smarthome.inmueble')),
            ],
        ),
    ]