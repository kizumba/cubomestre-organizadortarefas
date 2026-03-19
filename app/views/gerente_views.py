from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from app.models import Funcionario, Projeto, Cliente

class GerenteDashboard(View):
    template_name = "gerentes/dashboard_gerente.html"

    def get(self, request, *args, **kwargs):
        context = {}

        gerente = Funcionario.objects.get(pk=kwargs["pk"])
        projetos = Projeto.objects.filter(gerente=gerente)
        clientes = Cliente.objects.all()

        context.update({
            "projetos":projetos,
            "clientes":clientes,
            "gerente":gerente
            })

        return render(request, self.template_name, context)

class GerenteCriarProjeto(View):
    ...