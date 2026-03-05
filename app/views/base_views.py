from django.shortcuts import render

# Neste arquivo estão páginas como home, sobre, contatos etc.

def home(request):
    return render(request,"home.html")