from django.db import models

class Operacion(models.Model):
    
    num1 = models.CharField(max_length=25)
    num2 = models.CharField(max_length=25)
    resultado = models.CharField(max_length=50)