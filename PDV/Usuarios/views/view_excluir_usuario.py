from django.views import View
from Usuarios.repositories.r_usuario import RepositoriesUsuario
from django.shortcuts import render, redirect
from django.contrib import messages

class ExcluirUsuario(View):
    def __init__(self):
        self._usu = RepositoriesUsuario()

    def post(self, request):
        try:
            if not 'Usuario' in request.session:
                return redirect("loginUsuario")
            
            usuario = request.POST.dict()
            del usuario['csrfmiddlewaretoken']
            excluir = self._usu.excluirUsuario(id=usuario['usuarioid'])
            if excluir['Autorizado']:
                messages.success(request,f"Usuario {usuario['nome']} excluido com sucesso! ")
                return redirect("listarUsuario")
            else:
                messages.error(request,f"Error ao tentar excluir o usuário {usuario['nome']}")
        except Exception as error:
            messages.error(request, "Desculpe ocorreu um erro em nosso sistema tente novamente mais tarde!")
            return redirect("listarUsuario")

