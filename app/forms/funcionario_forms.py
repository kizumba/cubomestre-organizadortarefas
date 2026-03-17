from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import Funcionario, Endereco

class FuncionarioForm(UserCreationForm):
    data_nascimento = forms.DateField(required=False, widget=forms.DateInput(attrs={"type":"date"}))

    class Meta:
        model = Funcionario
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'data_nascimento', 'sexo', 'cpf', 'salario', 
            'cargo', 'telefone', 'habilidades',
            'is_staff', 'is_active',
        ]
    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Torna campos opcionais no formulário
            self.fields['data_nascimento'].required = False
            self.fields['sexo'].required = False
            self.fields['cpf'].required = False
            self.fields['telefone'].required = False
            self.fields['endereco'].required = False
            self.fields['salario'].required = False
            self.fields['cargo'].required = False
        
        def clean_cpf(self):
            cpf = self.cleaned_data.get('cpf')
            if cpf and Funcionario.objects.exclude(pk=self.instance.pk).filter(cpf=cpf).exists():
                raise forms.ValidationError('Este CPF já está cadastrado.')
            return cpf

class FuncionarioChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = Funcionario
        fields = [
            'username', 'first_name', 'last_name', 'email', 
            'is_staff', 'is_active', 'data_nascimento', 'sexo', 
            'cpf', 'salario', 'cargo', 'telefone', 'endereco',
            'habilidades'
        ]

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'data_contratacao': forms.DateInput(attrs={'type': 'date'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Torna campos opcionais
            self.fields['data_nascimento'].required = False
            self.fields['sexo'].required = False
            self.fields['cpf'].required = False
            self.fields['telefone'].required = False
            self.fields['endereco'].required = False
        
        def clean_username(self):
            username = self.cleaned_data['username']
            if self.instance and self.instance.pk and self.instance.username == username:
                return username
            if Funcionario.objects.filter(username=username).exists():
                raise forms.ValidationError('Um usuário com este nome de usuário já existe.')
            return username
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if self.instance and self.instance.pk and self.instance.username == username:
            return username
        if Funcionario.objects.filter(username=username).exists():
            raise forms.ValidationError('Um usuário com este nome de usuário já existe.')
        return username

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"
        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': '00000-000'}),
        }
