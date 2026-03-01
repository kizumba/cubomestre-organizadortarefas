from django.shortcuts import render

# Create your views here.
def teste_page(request):
    return render(request, "funcionarios/lista_funcionarios.html")

