from django.db import models
from django.utils import timezone


class City(models.Model):			                            # nombre de la tabla de la base de datos
    name=models.CharField(max_length = 100)	                    # atributos o columnas de la base “ciudades”
    description=models.TextField()
    image=models.ImageField(upload_to = 'citiesapp/photos')     # ubicacion de las imagenes
    population=models.IntegerField()
    country=models.CharField(max_length = 100)
    
    created_date=models.DateTimeField(default=timezone.now)     # ya importado el modulo arriba
    published_date=models.DateTimeField(blank=True, null=True)  # puede estar en blanco


    def __str__(self):
        return self.name            # self para referirme a la instancia y name para que me muestre el nombre


    class Meta:
        verbose_name_plural = 'Cities'          # atributo para los plurales (en este caso, de City)


