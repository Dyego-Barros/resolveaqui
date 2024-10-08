from django.shortcuts import render, redirect
from django.contrib import messages
from Produtos.repositories.r_produto import RepositorieProduto

class ProdutoView():

    def __init__(self):
        self._produ = RepositorieProduto() 
  
    def produto(self, request):
        if not 'Usuario' in request.session:
                return redirect("loginUsuario")
        try:
            if request.method =="GET":
                return render(request, "produto.html")    
        except Exception as error:
            raise ValueError(f"Error ao cerregar página de produtos, {error}")

     
   
    def cadastrarProduto(self, request):
        if not 'Usuario' in request.session:
            return redirect("loginUsuario")
        try:
            if request.method == "GET":
                return render(request, "cadastro_produto.html")
            
            elif request.method == "POST":
                produto = request.POST.dict()
                
                del produto['csrfmiddlewaretoken']
                produto['empresaid'] = request.session.get('Usuario', None).get('empresaid')
                print("Produto que vem do form", produto)
                cadastro = self._produ.cadastrarProduto(produto)
                if cadastro['Autorizado']:
                    messages.success(request,f"Produto {produto['nome']} cadastrado com sucesso!")
                    return redirect('listarProduto')
                else:
                    messages.error(request,f"Error ao cadastrar produto {produto['nome']}")
                    return redirect('cadastrarProduto')


        except Exception as error:
            pass
        #Verifica se o metodo é do tipo post
        
