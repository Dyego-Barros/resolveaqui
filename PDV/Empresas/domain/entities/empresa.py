
class Empresa():
    def __init__(self,razaosocial,cnpj,nomefantasia,nome,email,telefone,cpf,empresaid=None,ativo=None):
        self.empresaid = empresaid
        self.razaosocial = razaosocial
        self.cnpj = cnpj
        self.nomefantasia = nomefantasia
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.ativo= ativo
    
    def to_dict(self):
        return{
            "EmpresaId": self.empresaid,
            "RazaoSocial": self.razaosocial,
            "CNPJ": self.cnpj,
            "NomeFantasia": self.nomefantasia,
            "Nome": self.nome,
            "Email": self.email,
            "Telefone": self.telefone,
            "Cpf": self.cpf,
            "Ativo":self.ativo

        }