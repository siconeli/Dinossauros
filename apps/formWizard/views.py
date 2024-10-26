from pyexpat.errors import messages
from sqlite3 import IntegrityError
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from .forms import AlunoForm, ResponsavelForm, ContratoForm, FichaForm
from apps.contrato.models import Contrato
from django.urls import reverse
from django.db import transaction
import random
from django.contrib.auth.mixins import LoginRequiredMixin

FORMS = [
    ('aluno', AlunoForm),
    ('responsavel', ResponsavelForm),
    ('contrato', ContratoForm),
    ('ficha', FichaForm)
]

TEMPLATES = {
    'aluno': 'aluno/aluno_wizard_create.html',
    'responsavel': 'responsavel/responsavel_wizard_create.html',
    'contrato': 'contrato/contrato_wizard_create.html',
    'ficha': 'ficha/ficha_wizard_create.html'
}

class CadastroWizard(LoginRequiredMixin, SessionWizardView):
    form_list = FORMS

    # Define o método de armazenamento como sessão, no banco de dados.
    storage_name = 'formtools.wizard.storage.session.SessionStorage'

    def get_template_names(self) -> list[str]:
        return [TEMPLATES[self.steps.current]]
    
    def post(self, request, *args, **kwargs):
        try:
            # Verifica se o botão "Voltar" foi clicado
            if 'wizard_goto_step' in request.POST:
                # Obtém o passo para onde o usuário deseja ir
                goto_step  = request.POST.get('wizard_goto_step')
                return self.render_goto_step(goto_step)

            # Caso contrário, segue com o comportamento normal
            return super().post(request, *args, **kwargs)
        except Exception as e:
            print(e)

    @transaction.atomic
    def done(self, form_list, **kwargs):
        try:
            aluno_form = form_list[0]
            responsavel_form = form_list[1]
            contrato_form = form_list[2]
            ficha_form = form_list[3]

            criador = self.request.user

            aluno = aluno_form.save(commit=False)
            aluno.usuario_criador = criador
            aluno.save()

            responsavel = responsavel_form.save(commit=False)
            responsavel.usuario_criador = criador
            responsavel.autorizado = True
            responsavel.aluno = aluno
            responsavel.save()

            contrato = contrato_form.save(commit=False)
            if Contrato.objects.filter(ativo=True).exists():
                pk_db = Contrato.objects.filter(ativo=True).latest('pk').pk
            else:
                pk_db = -1

            contrato.numero = str(pk_db + 1) + str(random.randint(100, 999))
            contrato.usuario_criador = criador
            contrato.aluno = aluno
            contrato.save()

            ficha = ficha_form.save(commit=False)
            ficha.usuario_criador = criador
            ficha.aluno = aluno
            ficha.save()

            return redirect(reverse('aluno-detail', args=[aluno.pk]))
        
        except IntegrityError as e:
            messages.error(self.request, "Erro ao salvar dados " + str(e))
            print("Erro ao salvar dados " + str(e))

        except Exception as e:
        # Captura qualquer outro tipo de erro
            messages.error(self.request, "Um erro inesperado ocorreu: " + str(e))
            print("Um erro inesperado ocorreu: " + str(e))


