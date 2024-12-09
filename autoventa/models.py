from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# Modelo para la Marca
class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para el Modelo del Vehículo
class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='modelos')

    def __str__(self):
        return f"{self.nombre} - {self.marca.nombre}"


# Validación personalizada para el precio
def validar_precio(valor):
    if valor <= 0:
        raise ValidationError("El precio debe ser un número positivo.")


# Modelo para los Vehículos
class Vehiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='vehiculos')
    anio = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio])
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.modelo.nombre} ({self.anio})"


# Validación personalizada para el número de WhatsApp
def validar_whatsapp(valor):
    if not valor.startswith("+"):
        raise ValidationError("El número de WhatsApp debe comenzar con '+' seguido del código de país.")


# Modelo para el Contacto
class Contacto(models.Model):
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE, related_name='contacto')
    whatsapp = models.CharField(max_length=15, validators=[validar_whatsapp])

    def __str__(self):
        return f"Contacto para {self.vehiculo.modelo.nombre}: {self.whatsapp}"    