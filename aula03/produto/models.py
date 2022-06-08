from django.db import models

# Create your models here.
class produto(models.Model):
    nome = models.CharField(max_length=100)
    lote = models.IntegerField(max_length=100)
    validade = models.IntegerField(max_length=100)
    fabricante = models.CharField(max_length=100)
    codigo = models.IntegerField(max_length=100)

def str (self):
    return self.nome