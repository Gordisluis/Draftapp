from django.db import models



# Create your models here.
class players(models.Model):
    nombre = models.CharField(max_length=100)
    finales = models.IntegerField()
    finales_Ganadas = models.IntegerField()