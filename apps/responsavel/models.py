from django.db import models
from apps.aluno.models import Aluno
from apps.core.models import Base

class Responsavel(Base):
    sexo_choices = (
        ('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Outros', 'Outros')
    )
    
    parentesco_choices = (
        ('Pais', 'Pais'), ('Avós', 'Avós'), ('Tios', 'Tios'), ('Primos', 'Primos'), ('Outros', 'Outros')
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    autorizado = models.BooleanField(default=True)
    sexo = models.CharField(max_length=20, choices=sexo_choices)
    parentesco = models.CharField(max_length=20, choices=parentesco_choices)

    def __str__(self):
        return self.aluno