from django.db import models

# Create your models here.
class fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    mercadoria = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cnpj = models.IntegerField(max_length=11)

def str (self):
    return self.nome