# Generated by Django 5.0.2 on 2024-03-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=50)),
                ('telefono_empresa', models.IntegerField()),
                ('email_empresa', models.EmailField(max_length=254)),
                ('tipo_de_producto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=20)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('rol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.FloatField()),
                ('tipo', models.IntegerField()),
                ('tamanio', models.CharField(max_length=10)),
                ('gramaje', models.CharField(max_length=20)),
                ('rollos_metros', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('maquina', models.CharField(max_length=30)),
                ('tipo_tinta', models.CharField(max_length=50)),
                ('sublimacion', models.BooleanField()),
                ('materia', models.CharField(max_length=50)),
                ('catedra', models.CharField(max_length=50)),
            ],
        ),
    ]