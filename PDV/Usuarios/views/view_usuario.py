from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from Usuarios.repositories.r_usuario import RepositoriesUsuario

class Usuario(View):
    def __init__(self):
        self._usuario = RepositoriesUsuario()

    def get(self,request):
        return render(request,'login.html')

    def post(self, request):
        acao= request.POST.get('acao')
        if acao == 'Login':
            request.session['Tentativas'] = 0
            email = request.POST.get('email')            
            senha = request.POST.get('password')
            login = self._usuario.loginUsuario(email=email,senha=senha)
            if login['Autorizado']:
                print(login)
                request.session['Usuario'] = login['Usuario']
                #Salvando session
                request.session.modified = True
                return redirect("dashboard")
            else:
                if request.session['Tentativas'] == 3:
                    desativar = self._usuario.desativarUsuario(email=email)
                    if desativar:
                        messages.error(request,"Você excedeu as tentativas de login, seu usáriofoi bloqueado, contate o Administrador do sistema!")
                        return redirect("loginUsuario")
                    
                request.session['Tentativas'] = +1
                messages.error(request, f"Usuário ou senha inválidos! Tentativa {request.session['Tentativas']} de 3")
                return redirect("loginUsuario")
        elif acao == "CadastroUsuario":
            pass
        elif acao == 'logout':
            request.session.flush()
            return redirect('loginUsuario')

        



