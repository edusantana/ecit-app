from django.db import models
from core.models import Periodo

# https://docs.djangoproject.com/en/2.2/ref/models/fields/

class EletivaConfiguracao(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    inicio_selecao = models.DateTimeField("Data da selecao")
    quantidade_maxima = models.PositiveSmallIntegerField("Quantidade máxima de inscrições por eletiva")
    def __str__(self):
        return self.periodo.nome

    class Meta:
            verbose_name_plural = "configurações das eletivas"

class Eletiva(models.Model):
    configuracao = models.ForeignKey(EletivaConfiguracao, on_delete=models.CASCADE, related_name='eletivas')
    titulo = models.CharField('Título da eletiva', max_length=255)
    professores = models.CharField('Nomes dos professores da eletiva', max_length=255, default='')

    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    configuracao = models.ForeignKey(EletivaConfiguracao, on_delete=models.CASCADE, related_name='alunos')
    nome = models.CharField('Nome do aluno', max_length=255)
    turma = models.CharField('Turma do aluno', max_length=128, blank=True)
    senha = models.CharField('Senha para o aluno', max_length=32)
    eletiva = models.ForeignKey(Eletiva, on_delete=models.CASCADE, blank=True,
        null=True,related_name='alunos')

    def __str__(self):
        return self.nome
