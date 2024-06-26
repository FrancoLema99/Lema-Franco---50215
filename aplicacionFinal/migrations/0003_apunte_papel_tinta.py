# Generated by Django 5.0.2 on 2024-03-24 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionFinal', '0002_libreria_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apunte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=30)),
                ('catedra', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Papel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=30)),
                ('tamanio', models.CharField(max_length=10)),
                ('gramaje', models.CharField(max_length=20)),
                ('stock', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tinta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=30)),
                ('tipo_tinta', models.CharField(max_length=30)),
                ('sublimacion', models.BooleanField()),
                ('color', models.CharField(max_length=30)),
                ('stock', models.CharField(max_length=30)),
            ],
        ),
    ]
