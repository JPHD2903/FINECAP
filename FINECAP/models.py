from django.db import models

class Reserva(models.Model):
    cnpj = models.CharField(max_length=200)
    nome_empresa = models.CharField(max_length=200)
    categoria_empresa = models.CharField(max_length=200)
    quitado = models.BooleanField()

class Stand(models.Model):
    localizacao = models.CharField(max_length=500)
    valor = models.FloatField()
    

