from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.disponible}"

