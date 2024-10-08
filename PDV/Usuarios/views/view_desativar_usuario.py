from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from Usuarios.repositories.r_usuario import RepositoriesUsuario

class DesativarUsuario(View):
    def __init__(self):
        self._usu = RepositoriesUsuario()
    
    def post(self,request):
        try:
            if not 'Usuario' in request.session:
                return redirect("loginUsuario")
            usuario =request.POST.dict()

            if 'acao' in usuario:               
                del usuario['csrfmiddlewaretoken']
                ativar = self._usu.ativarUsuario(id=usuario['usuarioid'])
                
                if ativar['Autorizado']:
                    messages.success(request,f"Usuario {usuario['nome']} ativado com sucesso!")
                    return redirect("listarUsuario")
                else:
                    messages.error(request,f"Error ao ativar o usuário {usuario['nome']}")
                    return redirect("listarUsuario")
                
            del usuario['csrfmiddlewaretoken']
            desativar = self._usu.desativarUsuario(id=usuario['usuarioid'])
            if desativar['Autorizado']:
                messages.success(request,f"Usuario {usuario['nome']} desatvado com sucesso!")
                return redirect("listarUsuario")
            else:
                messages.error(request,f"Error ao desativa o usuário {usuario['nome']}")
                return redirect("listarUsuario")
        except Exception as error:
            messages.error(request,f"Desculpe ocorreu um erro em nosso sistema, tente novamente masi tarde!")
            return redirect("listarUsuario")
