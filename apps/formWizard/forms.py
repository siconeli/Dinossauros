from django import forms
from apps.aluno.models import Aluno
from apps.responsavel.models import Responsavel
from apps.contrato.models import Contrato
from apps.ficha.models import Ficha

class AlunoForm(forms.ModelForm):
    inativar = forms.BooleanField(required=False, label="inativar") # Colocado fora da classe Meta pois é um atributo que não faz parte do modelo Aluno, é utilizado apenas para receber um valor booleano que será utilizado na view de updateALuno, para ativar ou inativar um objeto ALuno.

    class Meta:
        model = Aluno

        fields = ['nome', 'cpf', 'idade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'nome', 'required': True}),
            'cpf': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'cpf', 'required': True}),
            'idade': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'max': 100, 'min': 1})
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Aluno.objects.filter(cpf=cpf).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('CPF já cadastrado.')
        return cpf
    
    def clean_idade(self):
        idade = self.cleaned_data.get('idade')
        if idade < 1:
            raise forms.ValidationError('Mínimo: 1 ano.')
        if idade > 100:
            raise forms.ValidationError('Máximo: 100 anos.')
        return idade
        
class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'profissao', 'sexo', 'parentesco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'required': True}),
            'cpf': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'cpf', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'telefone', 'required': True}),
            'endereco': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'endereco', 'required': True}),
            'profissao': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'profissao'}),
            'sexo': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'sexo', 'required': True}),
            'parentesco': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'parentesco', 'required': True}),
        }

    def clean_cpf(self): # Verificar cpf existente para não permitir duplicidade.
        cpf = self.cleaned_data.get('cpf')
        if Responsavel.objects.filter(cpf=cpf).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('CPF já cadastrado.')
        return cpf  

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['valor', 'periodo', 'data_inicio', 'data_fim']
        widgets = {
            'valor': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'valor', 'maxlength': 17, 'required': True}),
            'periodo': forms.Select(attrs={'class': 'form-control form-control-sm', 'id': 'periodo', 'required': True}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date', 'id': 'data_inicio', 'required': True}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date', 'id': 'data_fim', 'required': True})
        }
    
    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor < 1:
            raise forms.ValidationError('Este campo é obrigatório.')
        return valor

class FichaForm(forms.ModelForm):
    class Meta:
        model = Ficha
        fields = ['cuidado_especial', 'alergico', 'intolerante', 'quedas', 'refluxo', 'convulsoes', 'remedio_continuo', 'obs']
        widgets = {
            'obs': forms.Textarea(attrs={'class': 'form-control', 'maxlength': 2000})
        }
   