from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# ---------- Lista de productos ----------

# Artículos de librería

class Libreria(models.Model):
     
    nombre_producto = models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.FloatField()

    class Meta:

        ordering = ["nombre_producto"]


    def __str__(self):

        return f"{self.nombre_producto}"
    


# Papeles
     
class Papel(models.Model):
    
    marca = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    tamanio = models.CharField(max_length=10)
    gramaje = models.CharField(max_length=20)
    stock = models.CharField(max_length=30)

    def __str__(self):

        return f"{self.marca} {self.tipo}"


# Apuntes
    
class Apunte(models.Model):
     
    materia= models.CharField(max_length=50)
    catedra = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):

        return f"{self.materia}"

# Tintas
    
class Tinta(models.Model):
     
    marca = models.CharField(max_length=30)
    tipo_tinta = models.CharField(max_length=30) 
    color = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)

    def __str__(self):

        return f"{self.marca} {self.tipo_tinta}"




# ---------- Lista de empleados ----------
class Empleado(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()
    rol = models.CharField(max_length=50)


    class Meta:
        
        verbose_name = "Empleado/a"
        verbose_name_plural = "Empleados/as"
        ordering = ["apellido"]

    def __str__(self):
        
        return f"{self.apellido} {self.nombre}"




# ---------- Lista de clientes ----------
class Cliente(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()

    class Meta:
         
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["apellido"]

    def __str__(self):
              
        return f"{self.apellido} {self.nombre}"



# ---------- Contacto de proveedores ----------
class Contacto(models.Model):
    
    nombre_empresa = models.CharField(max_length=50)
    telefono_empresa = models.IntegerField()
    email_empresa = models.EmailField()
    tipo_de_producto = models.CharField(max_length=50)

    class Meta:
        
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ["nombre_empresa"]

    def __str__(self):
        
        return f"{self.nombre_empresa}"

# ---------- Avatar ---------- 
        
class Avatar(models.Model):
     
     imagen = models.ImageField(upload_to="avatares")
     user = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
          
          return f"{self.user} {self.imagen}"