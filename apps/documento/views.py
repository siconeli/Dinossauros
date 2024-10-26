from typing import Any
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from .models import Documento
from apps.aluno.models import Aluno
from django.contrib.auth.mixins import LoginRequiredMixin

class UploadDocumento(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            arquivo = request.FILES['arquivo']
            documento = Documento(
                usuario_criador=request.user,
                aluno=get_object_or_404(Aluno, id=pk),
                arquivo=arquivo
            )
            documento.save()

            documentos = Documento.objects.filter(aluno_id=pk)

            return render(request, 'fragmento/lista_documentos.html', {'documentos': documentos})
        except Exception as e:
            print(f'UploadDocumento -> {e}')

