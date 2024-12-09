from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, ModeloViewSet, VehiculoViewSet, ContactoViewSet, VehiculosPorPrecioAPIView

# Configuración del router
router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'modelos', ModeloViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'contactos', ContactoViewSet)

# Rutas personalizadas primero
urlpatterns = [
    path('vehiculos/por_precio/', VehiculosPorPrecioAPIView.as_view(), name='vehiculos_por_precio'),
]

# Rutas del router después
urlpatterns += [
    path('', include(router.urls)),
]
