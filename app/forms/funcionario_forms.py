from django.forms import ModelForm
from app.models import Funcionario, Endereco, Contato

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        exclude = ("contato", "endereco",)

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"
