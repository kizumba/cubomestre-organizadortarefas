from django.urls import path
from app.views.tipo_funcionario_views import (
    TipoFuncionarioListView,
    TipoFuncionarioCreateView,
    TipoFuncionarioUpdateView,
    TipoFuncionarioDeleteView,
)



urlpatterns = [
    path("lista_tipo_funcionarios", TipoFuncionarioListView.as_view(), name="lista_tipo_funcionarios"),
    path("form_tipo_funcionario", TipoFuncionarioCreateView.as_view(), name="criar_tipo_funcionario"),
    path("form_tipo_funcionario/<int:pk>", TipoFuncionarioUpdateView.as_view(), name="atualizar_tipo_funcionario"),
    path("apagar_tipo_funcionario/<int:pk>", TipoFuncionarioDeleteView.as_view(), name="apagar_tipo_funcionario"),
]
