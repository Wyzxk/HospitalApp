# Generated by Django 4.2.4 on 2024-03-31 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHospital', '0004_alter_doctores_foto_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctores',
            name='activo_d',
            field=models.CharField(max_length=8),
        ),
    ]
