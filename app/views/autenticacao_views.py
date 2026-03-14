from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    def get(self, request):
        data = {"form": AuthenticationForm}
        return render(request, "autenticacao/login.html", data)

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario:
            login(request, usuario)
            return redirect("home")
        else:
            form_login = AuthenticationForm()
            return render(
                request,
                "autenticacao/login.html",
                {"form": form_login, "error": "Usuário ou senha incorretos"},
            )

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
    
class AlterarSenhaView(LoginRequiredMixin, View):
    def get(self, request):
        data = {"form":PasswordChangeForm(request.user)}
        return render(request, "autenticacao/alterar_senha.html", data)

    def post(self, request):
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect("home")
        else:
            return render(request, "autenticacao/alterar_senha.html", {"form":form_senha})