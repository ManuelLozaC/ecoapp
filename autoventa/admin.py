from django.contrib import admin
from .models import Marca, Modelo, Vehiculo, Contacto

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca')
    list_filter = ('marca',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'anio', 'precio')
    list_filter = ('modelo__marca',)
    search_fields = ('modelo__nombre',)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'whatsapp')
