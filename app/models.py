from django.db import models

from django.db import models

class customer(models.Model):
  cpf = models.CharField(max_length=14)
  private = models.DecimalField(max_digits=5, decimal_places=2)
  incompleto = models.DecimalField(max_digits=5, decimal_places=2)
  data_da_ultima_compra = models.DateField()
  ticket_medio = models.FloatField()
  ticket_da_ultima_compra = models.FloatField()
  loja_mais_frequente = models.CharField(max_length=18)
  loja_da_ultima_compra = models.CharField(max_length=18)

  def __str__(self):
    return self.cpf