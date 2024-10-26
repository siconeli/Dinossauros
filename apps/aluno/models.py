from django.db import models
from apps.core.models import Base

class Aluno(Base):
    # foto = models.ImageField(upload_to='fotos/')
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
