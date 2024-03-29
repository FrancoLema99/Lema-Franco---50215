from django.contrib import admin
from .models import *

# Register your models here.


class LibreriaAdmin(admin.ModelAdmin):

    list_display = ("nombre_producto", "precio", "stock")
    list_filter = ("nombre_producto",)

class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ("nombre", "rol")

class ContactoAdmin(admin.ModelAdmin):

    list_display = ("nombre_empresa", "tipo_de_producto")
    list_filter = ("tipo_de_producto",)


admin.site.register(Libreria, LibreriaAdmin)
admin.site.register(Papel)
admin.site.register(Tinta)
admin.site.register(Apunte)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cliente)