from django.contrib import admin
from .models import Producto, Categoria

# Register your models here.
#admin.site.register(Producto)
class CategoriaAdmin(admin.ModelAdmin):
    list_filter = ('nombre',)
    search_fields = ('nombre',)


admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion', 'precio', 'stock', 'unidades', 'disponible', 'created', 'updated')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',  'disponible')
    list_editable = ('precio', 'stock', 'disponible')
    readonly_fields = ('created', 'updated')


admin.site.register(Producto, ProductoAdmin)
