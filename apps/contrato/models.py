from django.db import models
from apps.core.models import Base
from apps.aluno.models import Aluno

class Contrato(Base):
    periodo_choices = (
        ('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Integral', 'Integral')
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    valor = models.DecimalField(decimal_places=2, max_digits=11)
    periodo = models.CharField(max_length=20, choices=periodo_choices)
    data_inicio = models.DateField()
    data_fim = models.DateField() 

    def __str__(self):
        return self.numero