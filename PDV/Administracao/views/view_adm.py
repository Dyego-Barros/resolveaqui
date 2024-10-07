from django.views import View
from django.shortcuts import render, redirect

class AdmView(View):

    def get(self, request):
        if not 'Usuario' in request.session:                     
            return redirect("loginUsuario")
        
        Usuario = request.session.get('Usuario',None)  
        contexto = {
                "Usuario":Usuario
            }
        return render(request,'index.html',contexto)