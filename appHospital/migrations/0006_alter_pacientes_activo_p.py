# Generated by Django 4.2.4 on 2024-03-31 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHospital', '0005_alter_doctores_activo_d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='activo_p',
            field=models.CharField(max_length=8),
        ),
    ]
