from Produtos.domain.produtos import Produto
from Produtos.interfaces.Iproduto import IProduto
from Database.Database import Database
from uuid6 import uuid7

class RepositorieProduto(IProduto):
    def __init__(self):
        self._db = Database()

    def cadastrarProduto(self,produto:Produto):
        retorno = {}
        try:
           
            produtoid = str(uuid7())
            sql = """INSERT INTO produto (produtoid,nome,preco,quantidade,descricao,marca,empresaid,cod) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"""
            values=(produtoid, produto.nome,float(produto.preco),int(produto.quantidade), produto.descricao, produto.marca, produto.empresaid, produto.cod)
            cadastro = self._db.update_sql(sql=sql,values=values)
            print("Produto dentro de repositorio", produto)
            if cadastro:
                retorno['Autorizado'] = True
            else:
                retorno['Autorizado'] = False
            return retorno
         
        except Exception as error:
            print(error)
            retorno['Autorizado']=False
            return retorno
    
    def editarProduto(self, produto:Produto):
        pass

    def excluirProduto(self,id):
        pass

    def listarProduto(self):
        pass

    def obterProduto(self, id):
        pass