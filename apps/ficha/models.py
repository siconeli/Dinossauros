from django.db import models
from apps.core.models import Base
from apps.aluno.models import Aluno

class Ficha(Base):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    cuidado_especial = models.BooleanField(default=False, blank=True)
    alergico = models.BooleanField(default=False, blank=True)
    intolerante = models.BooleanField(default=False, blank=True)
    quedas = models.BooleanField(default=False, blank=True)
    refluxo = models.BooleanField(default=False, blank=True)
    convulsoes = models.BooleanField(default=False, blank=True)
    remedio_continuo = models.BooleanField(default=False, blank=True)
    obs = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.cuidado_especial