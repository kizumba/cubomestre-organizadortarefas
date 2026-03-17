from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from app.models import Funcionario, Endereco, Cliente, Projeto, Tarefa, Habilidade, FuncionarioHabilidade

from .models import (
    Funcionario, 
    Cliente,
    Projeto,
    Tarefa,
    Habilidade,
    FuncionarioHabilidade,
    Endereco,
)

class FuncionarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Funcionario
        fields = ('username', 'email', 'first_name', 'last_name', 'cargo')

class FuncionarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Funcionario
        fields = '__all__'

class FuncionarioAdmin(UserAdmin):
    form = FuncionarioChangeForm
    add_form = FuncionarioCreationForm
    
    # Campos a serem exibidos na lista
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'cargo')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'cargo')
    
    # Campos para o formulário de edição
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (_('Informações Pessoais'), {'fields': ('first_name', 'last_name', 'email', 
    #                                             'data_nascimento', 'sexo', 'cpf', 
    #                                             'telefone', 'endereco')}),
    #     (_('Informações Profissionais'), {'fields': ('cargo', 'salario', 'data_contratacao', 
    #                                                 'habilidades')}),
    #     (_('Permissões'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                  'groups', 'user_permissions')}),
    #     (_('Datas importantes'), {'fields': ('last_login', 'date_joined', 
    #                                        'criado_em', 'modificado_em')}),
    # )
    
    # Campos para o formulário de criação
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 
                      'password1', 'password2', 'cargo'),
        }),
        (_('Informações Pessoais'), {
            'classes': ('wide',),
            'fields': ('data_nascimento', 'sexo', 'cpf', 'telefone', 'endereco'),
        }),
    )
    
    search_fields = ('username', 'first_name', 'last_name', 'email', 'cpf')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions', 'habilidades')
    
    # Campos somente leitura
    readonly_fields = ('criado_em', 'modificado_em', 'last_login', 'date_joined')

# Register your models here.
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cliente)
admin.site.register(Habilidade)
admin.site.register(FuncionarioHabilidade)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Endereco)