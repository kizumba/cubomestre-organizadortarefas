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
)
from app.views.habilidade_views import (
    HabilidadeListView,
    HabilidadeCreateView,
)


urlpatterns = [
    path("lista_tipo_funcionarios", TipoFuncionarioListView.as_view(), name="lista_tipo_funcionarios"),
    path("form_tipo_funcionario", TipoFuncionarioCreateView.as_view(), name="criar_tipo_funcionario"),
    path("form_tipo_funcionario/<int:pk>", TipoFuncionarioUpdateView.as_view(), name="atualizar_tipo_funcionario"),
    path("apagar_tipo_funcionario/<int:pk>", TipoFuncionarioDeleteView.as_view(), name="apagar_tipo_funcionario"),
    # Funcionário
    path("form_funcionario", FuncionarioCreateView.as_view(),name="criar_funcionario"),
    path("lista_funcionarios", FuncionarioListView.as_view(), name="lista_funcionarios"),
    # Habilidade
    path("lista_habilidades", HabilidadeListView.as_view(), name="lista_habilidades"),
    path("form_habilidade", HabilidadeCreateView.as_view(),name="criar_habilidade"),
    path("detalhes_funcionario/<int:pk>", FuncionarioDetailView.as_view(), name="detalhes_funcionario"),
]
