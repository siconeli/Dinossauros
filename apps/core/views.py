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
            aluno = Aluno.objects.filter(nome__icontains=nome_filtro).order_by('-ativo', '-pk')

            for a in aluno:
                if a.ativo is True:
                    a.ativo = 'Ativo'
                else:
                    a.ativo = 'Inativo'
            context['alunos'] = aluno
        else:
            aluno = Aluno.objects.all().order_by('-ativo', '-pk')

            for a in aluno:
                if a.ativo is True:
                    a.ativo = 'Ativo'
                else:
                    a.ativo = 'Inativo'
            context['alunos'] = aluno

        return context

