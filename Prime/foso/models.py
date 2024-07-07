from django.db import models


#club se refiere al equipo del jugador en el torneo
# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    goles = models.IntegerField()

