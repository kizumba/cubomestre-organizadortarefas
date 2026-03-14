from django.contrib import admin

from .models import (
    Funcionario, 
    Cliente,
    Projeto,
    Tarefa,
    Habilidade,
    FuncionarioHabilidade,
    Endereco,
)

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Habilidade)
admin.site.register(FuncionarioHabilidade)
admin.site.register(Projeto)
admin.site.register(Tarefa)
admin.site.register(Endereco)