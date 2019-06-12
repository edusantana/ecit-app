from django.db import models

class Inscricao(models.Model):
    titulo = models.CharField('Título', max_length=255)
    inicio = models.DateTimeField("Data e hora para início das inscrições")
    resposta_textual = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
            verbose_name_plural = "inscrições"

class Alternativa(models.Model):
    inscricao = models.ForeignKey(Inscricao,
        on_delete=models.CASCADE, related_name='alternativas')
    quantidade_maxima = models.PositiveSmallIntegerField("Quantidade máxima de inscrições")
    titulo = models.CharField('Título', max_length=255)
    url = models.URLField('Link para mais informações', blank=True, default='')

    def __str__(self):
        return self.titulo

    def inscreve(self, participante):
        if participante.alternativa == self:
            raise InscricaError('Participante já estava inscrito')
        elif self.quantidade_maxima <= self.participantes.count():
            raise InscricaError('Não há mais vagas.')
        else:
            participante.alternativa = self
            participante.save()

class InscricaError(RuntimeError):
    pass

class Participante(models.Model):
    inscricao = models.ForeignKey(Inscricao,
        on_delete=models.CASCADE, related_name='participantes')
    matricula = models.IntegerField('Matrícula', blank=True, null=True)
    nome = models.CharField('Nome', max_length=255)
    senha = models.CharField('Senha para inscrição', max_length=32)
    turma = models.CharField('Turma', max_length=128, blank=True, default='')
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE, blank=True, null=True,
        related_name='participantes')
    resposta = models.CharField('Resposta', max_length=255, blank=True, default='')

    def __str__(self):
        return self.nome
