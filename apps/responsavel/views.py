from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from apps import responsavel

from .models import Aluno
from apps.formWizard.forms import ResponsavelForm
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Responsavel

class ResponsavelCreate(LoginRequiredMixin, CreateView):
    model = Responsavel
    template_name = 'responsavel/responsavel_create.html'
    form_class = ResponsavelForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        try:
            form.instance.usuario_criador = self.request.user
            form.instance.aluno = Aluno.objects.get(pk=self.kwargs.get('pk'))
            form.instance.autorizado = True
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return render(self.request, 'responsavel/responsavel_create.html', {'form':form})

    def cancelar(self, aluno_pk):
        try:
            return reverse('aluno-detail', args=[aluno_pk])
        except Exception as e:
            print(e)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        try:
            context = super().get_context_data(**kwargs)
            context['cancelar'] = self.cancelar(self.kwargs.get('pk'))
            return context
        except Exception as e:
            print(e)
        
    def get_success_url(self) -> str:
        try:
            return reverse('aluno-detail', args=[self.kwargs.get('pk')])
        except Exception as e:
            print(e)

class ResponsavelDelete(LoginRequiredMixin, DeleteView):
    model = Responsavel

    def get_success_url(self) -> str:
        try:
            responsavel = self.model.objects.get(id=self.kwargs.get('pk'))
            return reverse('aluno-detail', args=[responsavel.aluno_id])
        except Exception as e:
            print(e)