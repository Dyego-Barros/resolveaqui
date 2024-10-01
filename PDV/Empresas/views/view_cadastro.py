from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from Empresas.repositories.r_empresa import RepositorieEmpresa
from Empresas.domain.entities.empresa import Empresa

class Empresa(View):
    def __init__(self):      
        self._empresa = RepositorieEmpresa()     

    def get(self,request):
        return render(request,'cadastro.html')    

    def post(self,request):
        if request.method == 'POST':
            dados = request.POST.dict() 
            retorno = self._empresa.cadastrar_empresa(dados)
            if retorno:
                messages.success(request, "Empresa Cadastrada com sucesso! Você receberá um e-mail com instruções para realizar o login em nossa platsaforma!")
                return redirect("loginUsuario")
            else:
                messages.error(request,"Falha ao cadatrar empresa, tente novamente mais tarde!")
            
        return redirect('cadastro')
    
    def put(self,request):
        if request.method =='PUT':
            dados = request.PUT.dict()
            pass