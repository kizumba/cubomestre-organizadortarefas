from django.forms import ModelForm
from app.models import Cliente, Endereco, Contato

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ("contato", "endereco",)

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"
