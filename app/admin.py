from django.contrib import admin

from .models import (
    Funcionario, 
    TipoFuncionario,
    Cliente,
    TipoCliente,
    Projeto,
    Tarefa,
    Habilidade,
    FuncionarioHabilidade,
    Contato,
    Endereco,
)

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(TipoFuncionario)
admin.site.register(Cliente)
admin.site.register(TipoCliente)
admin.site.register(Habilidade)
admin.site.register(FuncionarioHabilidade)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Contato)
admin.site.register(Endereco)