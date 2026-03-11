from django.urls import path
from app.views.tipo_funcionario_views import (
    TipoFuncionarioListView,
    TipoFuncionarioCreateView,
    TipoFuncionarioUpdateView,
    TipoFuncionarioDeleteView,
)
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
)

urlpatterns = [
    # Tipo de funcionário
    path("lista_tipo_funcionarios", TipoFuncionarioListView.as_view(), name="lista_tipo_funcionarios"),
    path("form_tipo_funcionario", TipoFuncionarioCreateView.as_view(), name="criar_tipo_funcionario"),
    path("form_tipo_funcionario/<int:pk>", TipoFuncionarioUpdateView.as_view(), name="atualizar_tipo_funcionario"),
    path("apagar_tipo_funcionario/<int:pk>", TipoFuncionarioDeleteView.as_view(), name="apagar_tipo_funcionario"),

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
    path("form_projeto", ProjetoCreateView.as_view(), name="criar_projeto"),
]
