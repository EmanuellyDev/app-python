from django.db import models

# Create your models here.
class notaFiscal(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    valor = models.IntegerField(max_length=1000000000)
    cpf = models.IntegerField(max_length=11)

def str (self):
    return self.nome