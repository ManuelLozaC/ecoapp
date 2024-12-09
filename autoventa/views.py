#from django.shortcuts import render
from rest_framework import viewsets
from .models import Marca, Modelo, Vehiculo, Contacto
from .serializers import MarcaSerializer, ModeloSerializer, VehiculoSerializer, ContactoSerializer

# ViewSet para Marca
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


# ViewSet para Modelo
class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


# ViewSet para Vehiculo
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


# ViewSet para Contacto
class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vehiculo

class VehiculosPorPrecioAPIView(APIView):
    def get(self, request, *args, **kwargs):
        max_precio = request.query_params.get('max_precio', None)
        if max_precio:
            vehiculos = Vehiculo.objects.filter(precio__lte=max_precio)
        else:
            vehiculos = Vehiculo.objects.all()
        data = [{"modelo": v.modelo.nombre, "precio": v.precio} for v in vehiculos]
        return Response(data)
