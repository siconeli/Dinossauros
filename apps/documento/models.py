from django.db import models
from apps.core.models import Base
from apps.aluno.models import Aluno

class Documento(Base):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return self.arquivo
