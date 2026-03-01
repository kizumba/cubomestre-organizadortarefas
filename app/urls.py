from django.urls import path
from .views import teste_page

urlpatterns = [
    path("funcionarios/", teste_page,name="lista_funcionarios"),
]
