# Generated by Django 5.0.2 on 2024-03-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionFinal', '0006_alter_libreria_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='rol',
            field=models.CharField(max_length=50),
        ),
    ]