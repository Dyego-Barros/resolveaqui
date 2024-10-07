from typing import Any
from django.views import View
from django.shortcuts import render, redirect
from Usuarios.repositories.r_usuario import RepositoriesUsuario 
from django.contrib import messages

class Usuario(View):
    def __init__(self):
        self._usu = RepositoriesUsuario()

    def get(self, request):
        if "Usuario" not in request.session:
            return redirect("loginUsuario")          
        perfil = self._usu.ObterPerfil()
        usuario = request.session.get('Usuario',None)
        contexto ={"Perfil": perfil,"Usuario":usuario}        
        return render(request,'cadastro_usuario.html', contexto)
    
    def post(self, request):
        try: 
            if "Usuario" not in request.session:
                return redirect("loginUsuario")  
            
            usuario = request.POST.dict()
            del usuario['csrfmiddlewaretoken']#Deleta middlewaretoken que não é usado    

            usuario['empresaid'] = request.session.get('Usuario').get('empresaid')
            insert = self._usu.cadastrarUsuario(usuario=usuario)

            if insert['Autorizado']:
                messages.success(request,"Usuário cadastrado com sucesso!")
                return redirect("listarUsuario")
            else:
                messages.error(request,"Error ao cadastrar novo usuário!")
                return redirect("cadastrarUsuario")
            
        except Exception as erro:
            messages.error(request,"Desculpe nosso serviço obteve um error inesperado, tentenovamente mais tarde!")
            return redirect("cadastrarUsuario")
    
    


          

       