from django.views import View
from Usuarios.repositories.r_usuario import RepositoriesUsuario
from django.shortcuts import render, redirect
from django.contrib import messages
class listarUsuario(View):
    def __init__(self):
        self._usu= RepositoriesUsuario()

    def get(self,request):
        if not 'Usuario' in request.session:
            return redirect("loginUsuario")
                
        usuario = request.session.get('Usuario',None)
        perfil = self._usu.ObterPerfil()
        lista_usuario =self._usu.listarUsuario(empresaid=usuario['empresaid'])
        contexto = {
            "Usuario": usuario,
            "Perfil": perfil,
            "Usuarios": lista_usuario
        }
        return render(request,"listar_usuario.html",contexto)
    
    def post(self,request):
        try:
            if not 'Usuario' in request.session:
                return redirect("loginUsuario")
            
            usuario = request.POST.dict()
           
            del usuario['csrfmiddlewaretoken']
            
            usuario['empresaid'] = request.session.get('Usuario').get('empresaid')
            editaUsuario = self._usu.editarUsuario(usuario=usuario)

            if editaUsuario['Autorizado']:
                messages.success(request,"Usuário Editado com sucesso!")
                return redirect("listarUsuario")
            else:
                messages.error(request,"Error ao Editar usuário, tente novamente mais tarde!")
                return redirect("listarUsuario")
        except Exception as error:
            print(error)
            messages.error(request,"Ocorreu um error inesperado ao editar usuário, tente novamente mais tarde!")
            return redirect("listarUsuario")