from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Aluno
from apps.formWizard.forms import ResponsavelForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Responsavel

class ResponsavelCreate(LoginRequiredMixin, CreateView):
    model = Responsavel
    template_name = 'responsavel/responsavel_create.html'
    form_class = ResponsavelForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        try:
            responsavel = get_object_or_404(self.model, pk=self.kwargs.get('pk'))
            form.instance.usuario_criador = self.request.user
            form.instance.aluno = Aluno.objects.get(pk=self.kwargs.get('pk'))
            form.instance.autorizado = True
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return render(self.request, 'responsavel/responsavel_create.html', {'form':form, 'responsavel': responsavel})

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