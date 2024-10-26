from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.aluno.models import Aluno

class InicioView(LoginRequiredMixin, TemplateView):
    template_name = 'core/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        nome_filtro = self.request.GET.get('nome_filtro')

        if nome_filtro:
            context['alunos'] = Aluno.objects.filter(ativo=True, nome__icontains=nome_filtro).order_by('-pk')
        else:
            context['alunos'] = Aluno.objects.filter(ativo=True).order_by('-pk')

        return context

