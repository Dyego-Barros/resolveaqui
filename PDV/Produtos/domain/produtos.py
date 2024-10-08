
class Produto():
    def __init__(self,nome,preco,quantidade,descricao,marca,cod, empresaid,produtoid=None):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.descricao = descricao
        self.marca = marca
        self.cod = cod
        self.empresaid = empresaid
        self.produtoid = produtoid

    def todic(self):
        return {
            "nome":self.nome,
            "preco":self.preco,
            "quantidade": self.quantidade,
            "descricao": self.descricao,
            "marca": self.marca,
            "cod":self.cod,
            "empresaid": self.empresaid,
            "produtoid":self.produtoid
        }
