# Generated by Django 3.1.7 on 2021-05-26 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smarthome', '0002_auto_20210524_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='smarthome/images/')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='smarthome.inmueble')),
            ],
        ),
        migrations.DeleteModel(
            name='Imagenes',
        ),
    ]
