from django import forms
from app.models import Projeto, Funcionario


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gerente"].queryset = Funcionario.objects.filter(cargo=2)
        self.fields["gerente"].label_from_instance = self.label_from_instance_fruncionario

    def label_from_instance_fruncionario(self, obj):
        return f"{obj.get_full_name()} - {obj.get_cargo_display()}"
