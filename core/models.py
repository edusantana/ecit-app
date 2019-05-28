from django.db import models

# Create your models here.

class Escola(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome
class Periodo(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    ativo = models.BooleanField(max_length=255, default=True)

    def __str__(self):
        return self.nome
