from typing import Any
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import DeleteView
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
            for doc in documentos:
                doc.nome = str(doc.arquivo)[11:]

            return render(request, 'fragmento/lista_documentos.html', {'documentos': documentos})
        except Exception as e:
            print(f'UploadDocumento -> {e}')

class DocumentoDelete(LoginRequiredMixin, DeleteView):
    model = Documento

    def get_success_url(self):
        documento = self.model.objects.get(id=self.kwargs.get('pk'))
        return reverse('aluno-detail', args=[documento.aluno_id])