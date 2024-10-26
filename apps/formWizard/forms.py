from django import forms
from apps.aluno.models import Aluno
from apps.responsavel.models import Responsavel
from apps.contrato.models import Contrato
from apps.ficha.models import Ficha

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'idade']
        widgets = {
            'cpf': forms.TextInput(attrs={'id': 'cpf'}),
            'idade': forms.NumberInput(attrs={'max': 100, 'min': 1})
        }

        def clean_cpf(self):
            cpf = self.cleaned_data.get('cpf')
            if Aluno.objects.filter(cpf=cpf).exists():
                raise forms.ValidationError('Esse CPF já está cadastrado. Por favor, insira um CPF único.')
            return cpf
        
class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'profissao', 'sexo', 'parentesco']
        widgets = {
            'cpf': forms.TextInput(attrs={'id': 'cpf'}),
            'telefone': forms.TextInput(attrs={'id': 'telefone'})
        }

    def clean_cpf(self): # Verificar cpf existente para não permitir duplicidade.
        cpf = self.cleaned_data.get('cpf')
        if Responsavel.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Esse CPF já está cadastrado. Por favor, insira um CPF único.')
        return cpf  

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['valor', 'periodo', 'data_inicio', 'data_fim']
        widgets = {
            'valor': forms.TextInput(attrs={'id': 'valor'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'})
        }

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['cuidado_especial', 'alergico', 'intolerante', 'quedas', 'refluxo', 'convulsoes', 'remedio_continuo', 'obs']