from django import forms
from django.core.exceptions import ValidationError
from app.models import Tarefa, Funcionario


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        habilidade_id = None

        if self.data.get("habilidade"):
            habilidade_id = self.data.get("habilidade")
        elif self.instance and self.instance.pk and self.instance.habilidade:
            habilidade_id = self.instance.habilidade.id
        
        queryset = Funcionario.objects.filter(cargo=3)

        if habilidade_id:
            queryset = queryset.filter(habilidades__id=habilidade_id)

        self.fields["colaborador"].queryset = queryset
        self.fields["colaborador"].label_from_instance = self.label_from_instance_funcionario

        if queryset.count() == 0 and habilidade_id:
            self.fields["colaborador"].empty_label = "Nenhum colaborador com esta habilidade disponível."

    def label_from_instance_funcionario(self, obj):
        habilidades = ", ".join([h.nome for h in obj.habilidades.all()[0:3]])
        return f"{obj.get_full_name()} - {obj.get_cargo_display()} (Habilidades: {habilidades})"
    
    def clean(self):
        cleaned_data = super().clean()
        colaborador = cleaned_data.get("colaborador")
        habilidade = cleaned_data.get("habilidade")

        if colaborador and habilidade:
            if not colaborador.habilidades.filter(id=habilidade.id).exists():
                raise ValidationError(
                    f"O colaborador {colaborador.get_full_name()} não possui a habilidade {habilidade.nome}"
                )
            return cleaned_data