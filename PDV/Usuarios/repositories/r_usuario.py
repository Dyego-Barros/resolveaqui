from Usuarios.domain.entities.Usuario import Usuario
from Usuarios.interfaces.Iusuario import IUsuario
from Database.Database import Database
from PDV.config import cripto
from cryptocode import decrypt, encrypt
from traceback import format_exc as exec

class RepositoriesUsuario(IUsuario):
    def __init__(self):
        self._db= Database()
        

    def cadastrarUsuario(self, usuario:dict):
        pass

    def editarUsuario(self,usuario:dict):
        return super().editarUsuario()
    
    def listarUsuario(self):
        return super().listarUsuario()
    
    def excluirUsuario(self,id):
        return super().excluirUsuario()
    
    def obterUsuario(self,id):
        return super().obterUsuario()
    
    def loginUsuario(self,email,senha):
        retorno = {}
        sql = """SELECT usuarioid,nome,email,funcao,cargo,senha,perfilid,empresaid FROM public.usuario WHERE email=%s and ativo=1;"""     
        values= (email,)       
        dados = self._db.execute_sql(sql=sql, values=values)       
        if len(dados) == 0:            
            retorno['Autorizado'] = False
            retorno['Mensagem'] = "Usuário não encontrado!"
            retorno['Usuario'] = []
            return retorno        
        dados = dados[0]
        
        senhadecripto = decrypt(dados['senha'],cripto())
        print(senhadecripto, senha)
        if senhadecripto == senha:
            retorno['Autorizado']= True
            retorno['Usuario'] = {
               "usuarioid":str(dados['usuarioid']),
               "nome":dados['nome'],
               "email":dados['email'],
               "funcao":dados['funcao'],
               "cargo":dados['cargo'],
               "senha": dados['senha'],
               "perfilid": str(dados['perfilid']),
               "empresaid": str(dados['empresaid'])
            }
            return retorno
        else:
            retorno['Autorizado']= False
            retorno['Mensagem']= "Usuário ou senha incorretos!"
            return retorno
    
    def desativarUsuario(self,email):
        try:
            retorno = {}
            sql = """UPDATE public.usuario ativo=0 WHERE email =%s;"""
            values= (email,)
            upd = self._db.update_sql(sql,values)
            if upd:
                retorno['Autorizado'] = True
                return retorno
        except Exception as error:
            print("Error %s  \n Rastreio %s", error, exec())
            retorno['Autorizado'] = False
            return retorno

        

        
       