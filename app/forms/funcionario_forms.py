from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import Funcionario, Endereco

class FuncionarioForm(UserCreationForm):
    class Meta:
        model = Funcionario
        exclude = ("password","endereco","groups","user_permissions","is_superuser","last_login","data_joined")
    
class FuncionarioChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = Funcionario
        fields = ['username', 'first_name', 'last_name', 'email', 
                  'is_staff', 'is_active', 'data_nascimento', 'sexo', 
                  'cpf', 'salario', 'cargo', 'telefone', 'habilidades']
    
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
