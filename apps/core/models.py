from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True)
    usuario_criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
