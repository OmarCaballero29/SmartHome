# Generated by Django 3.1.7 on 2021-06-04 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smarthome', '0011_auto_20210603_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='propietario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
