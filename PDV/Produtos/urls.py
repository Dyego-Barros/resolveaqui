from django.urls import path
from .view.produto_view import ProdutoView

produto = ProdutoView()
urlpatterns=[
    path("", produto.produto, name="listarProduto"),
    path("cadastrar", produto.cadastrarProduto, name="cadastrarProduto")
]