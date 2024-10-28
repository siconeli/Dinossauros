from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Aluno
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.contrato.models import Contrato
from apps.ficha.models import Ficha
from apps.responsavel.models import Responsavel
from django.urls import reverse
from apps.documento.models import Documento
from apps.formWizard.forms import AlunoForm

class AlunoDetail(LoginRequiredMixin, DetailView):
    model = Aluno
    template_name = 'aluno/aluno_detail.html'

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        try:
            return  get_object_or_404(Aluno, id=self.kwargs.get('pk'))
        except Exception as e:
            print(f'get_object - AlunoDetail -> {e}')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            context = super().get_context_data(**kwargs)
            aluno_pk_uri = self.kwargs.get('pk')

            documentos = Documento.objects.filter(aluno_id=aluno_pk_uri)
            for doc in documentos:
                doc.nome = str(doc.arquivo)[11:]

            context['contrato'] = get_object_or_404(Contrato, aluno_id=aluno_pk_uri)
            context['ficha'] = get_object_or_404(Ficha, aluno_id=aluno_pk_uri)
            context['responsaveis'] = Responsavel.objects.filter(aluno_id=aluno_pk_uri)
            context['aluno_pk'] = aluno_pk_uri
            context['documentos'] = documentos
            return context
        except Exception as e:
            print(f'get_context_data - AlunoDetail -> {e}')

class AlunoUpdate(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            aluno = get_object_or_404(Aluno, id=pk)
            form = AlunoForm(request.POST, instance=aluno)

            if form.is_valid():
                if Aluno.objects.filter(cpf=form.cleaned_data['cpf']).exclude(id=pk).exists():
                    return render(request, 'fragmento/aluno_update.html', {'form': form, 'aluno': aluno})

                form.save()
                return render(request, 'fragmento/aluno_update.html', {'aluno': aluno})

            return render(request, 'fragmento/aluno_update.html', {'form': form, 'aluno': aluno})
        
        except Exception as e:
            print(f'AlunoUpdate -> {e}')
            return render(request, 'fragmento/aluno_update.html', {'form': form, 'aluno': aluno})

class AlunoDelete(LoginRequiredMixin, DeleteView):
    model = Aluno

    def get_success_url(self):
        try:
            return reverse('inicio')
        except Exception as e:
            print(e)