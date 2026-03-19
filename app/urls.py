from django.urls import path

from app.views.funcionario_views import (
    FuncionarioCreateView,
    FuncionarioListView,
    FuncionarioDetailView,
    FuncionarioUpdateView,
    FuncionarioDeleteView,
)
from app.views.habilidade_views import (
    HabilidadeListView,
    HabilidadeCreateView,
    HabilidadeUpdateView,
    HabilidadeDeleteView,
)
from app.views.cliente_views import (
    ClienteListView,
    ClienteCreateView,
    ClienteDetailView,
    ClienteUpdateView,
    ClienteDeleteView,
)
from app.views.projeto_views import (
    ProjetoListView,
    ProjetoCreateView,
    ProjetoUpdateView,
    ProjetoDetailView,
    ProjetoDeleteView,
)
from app.views.tarefa_views import(
    TarefaListView,
    TarefaCreateView,
    TarefaUpdateView,
    TarefaDetailView,
    TarefaDeleteView,
)

from app.views.autenticacao_views import (
    LoginView,
    LogoutView,
    AlterarSenhaView,
)

from app.views.gerente_views import GerenteDashboard

urlpatterns = [   
    # Funcionário
    path("form_funcionario", FuncionarioCreateView.as_view(),name="criar_funcionario"),
    path("lista_funcionarios", FuncionarioListView.as_view(), name="lista_funcionarios"),
    path("detalhes_funcionario/<int:pk>", FuncionarioDetailView.as_view(), name="detalhes_funcionario"),
    path("form_funcionario/<int:pk>", FuncionarioUpdateView.as_view(),name="atualizar_funcionario"),
    path("apagar_funcionario/<int:pk>", FuncionarioDeleteView.as_view(),name="apagar_funcionario"),

    # Habilidade
    path("lista_habilidades", HabilidadeListView.as_view(), name="lista_habilidades"),
    path("form_habilidade", HabilidadeCreateView.as_view(),name="criar_habilidade"),
    path("form_habilidade/<int:pk>", HabilidadeUpdateView.as_view(), name="atualizar_habilidade"),
    path("apagar_habilidade/<int:pk>", HabilidadeDeleteView.as_view(), name="apagar_habilidade"),

    # Clientes
    path("lista_clientes", ClienteListView.as_view(), name="lista_clientes"),
    path("form_cliente", ClienteCreateView.as_view(), name="criar_cliente"),
    path("detalhes_cliente/<int:pk>", ClienteDetailView.as_view(), name="detalhes_cliente"),
    path("form_cliente/<int:pk>", ClienteUpdateView.as_view(),name="atualizar_cliente"),
    path("apagar_cliente/<int:pk>", ClienteDeleteView.as_view(), name="apagar_cliente"),

    # Projetos
    path("lista_projetos", ProjetoListView.as_view(), name="lista_projetos"),
    path("form_projeto>", ProjetoCreateView.as_view(), name="criar_projeto"),
    path("form_projeto/<int:pk>", ProjetoUpdateView.as_view(), name="atualizar_projeto"),
    path("detalhes_projeto/<int:pk>", ProjetoDetailView.as_view(), name="detalhes_projeto"),
    path("apagar_projeto/<int:pk>", ProjetoDeleteView.as_view(), name="apagar_projeto"),

    #
    path("lista_tarefas", TarefaListView.as_view(), name="lista_tarefas"),
    path("form_tarefa>", TarefaCreateView.as_view(), name="criar_tarefa"),
    path("form_tarefa/<int:pk>", TarefaUpdateView.as_view(), name="atualizar_tarefa"),
    path("detalhes_tarefa/<int:pk>", TarefaDetailView.as_view(), name="detalhes_tarefa"),
    path("apagar_tarefa/<int:pk>", TarefaDeleteView.as_view(), name="apagar_tarefa"),

    # Login
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("alterar_senha", AlterarSenhaView.as_view(), name="alterar_senha"),

    # Gerente Dashboard
    path("gerente/<int:pk>", GerenteDashboard.as_view(), name="gerente_dashboard"),

]
