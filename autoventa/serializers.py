from rest_framework import serializers
from .models import Marca, Modelo, Vehiculo, Contacto

# Serializador para Marca
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'


# Serializador para Modelo
class ModeloSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = Modelo
        fields = '__all__'


# Serializador para Vehiculo
class VehiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer()

    class Meta:
        model = Vehiculo
        fields = '__all__'


# Serializador para Contacto
class ContactoSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()

    class Meta:
        model = Contacto
        fields = '__all__'
