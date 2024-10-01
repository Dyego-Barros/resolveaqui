
class Usuario():
    def __init__(self,nome, email,funcao,cargo,senha,ativo,perfilid,empresaid,usuarioid=None):
        self.usuarioid = usuarioid
        self.nome = nome
        self.email = email
        self.funcao = funcao
        self.cargo = cargo
        self.senha = senha
        self.ativo = ativo
        self.perfilid = perfilid
        self.empresaid = empresaid

    def to_dict(self):
        return {
            "usuarioid": self.usuarioid,
            "nome": self.nome,
            "email": self.email,
            "funcao": self.funcao,
            "cargo":self.cargo,
            "senha": self.senha,
            "ativo": self.ativo,
            "perfilid": self.perfilid,
            "empresaid":self.empresaid
        }