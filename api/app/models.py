from django.db import models

class Transacao(models.Model):
    estabelecimento = models.CharField(max_length=14)
    cliente =  models.CharField(max_length=11)
    valor = models.FloatField()
    descricao =  models.CharField(max_length=255)

    class Meta:
        verbose_name = "Transacao"
        verbose_name_plural = "Transacoes"

