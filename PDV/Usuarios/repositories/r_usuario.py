from Usuarios.domain.entities.Usuario import Usuario
from Usuarios.interfaces.Iusuario import IUsuario
from Database.Database import Database
from PDV.config import cripto
from cryptocode import decrypt, encrypt
from traceback import format_exc as exec
from uuid6 import uuid7

class RepositoriesUsuario(IUsuario):
    def __init__(self):
        self._db= Database()
        

    def cadastrarUsuario(self, usuario:dict):
        retorno = {}
        try:            
            newUsuario = Usuario(**usuario)
            usuarioid = uuid7()
            newUsuario.usuarioid = str(usuarioid)
            sql=""" INSERT  INTO usuario (usuarioid,nome,email,funcao,cargo,senha,ativo,perfilid,empresaid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
            senhacripto = encrypt(newUsuario.senha, cripto())
            values = (newUsuario.usuarioid, newUsuario.nome, newUsuario.email, newUsuario.funcao,newUsuario.cargo,senhacripto,int(newUsuario.ativo),newUsuario.perfilid,newUsuario.empresaid)
            insert = self._db.update_sql(sql=sql,values=values)
            print(insert)
            if insert:
                retorno['Autorizado'] = True
            else:
                retorno['Autorizado']= False

            return retorno
        except Exception as error:
            retorno['Autorizado']= False
            print(error)
            return retorno

    def editarUsuario(self,usuario:dict):
        retorno = {}
        try:
            print("Usuario a ser editado", usuario)
            editarUsuario = Usuario(**usuario)
            senhaCripto = encrypt(editarUsuario.senha, cripto())
            sql = """UPDATE usuario SET nome=%s, email=%s, funcao=%s, cargo=%s, senha=%s, ativo=%s, perfilid=%s WHERE usuarioid=%s and empresaid=%s;"""
            values= (editarUsuario.nome, editarUsuario.email, editarUsuario.funcao, editarUsuario.cargo, senhaCripto, int(editarUsuario.ativo),editarUsuario.perfilid, editarUsuario.usuarioid, editarUsuario.empresaid)
            editar = self._db.update_sql(sql=sql,values=values)
            if editar:
                retorno['Autorizado'] = True
                return retorno
            else:
                retorno['Autorizado'] = False
                return retorno

        except Exception as error:
            print(error)
            retorno['Autorizado']= False
            return retorno
    
    def listarUsuario(self,empresaid):
        try:
            sql="""SELECT us.usuarioid,us.nome,us.email,us.funcao,us.cargo,us.ativo,us.perfilid, pf.perfil from usuario as us inner join perfil as pf on us.perfilid = pf.perfilid WHERE us.empresaid =%s;"""
            values =(empresaid, )
            lista_usuarios = self._db.execute_sql(sql=sql,values=values)
            print(lista_usuarios)
            if lista_usuarios:
                return lista_usuarios
            else:
                lista_usuarios = []
                return list
        except Exception as error:
            lista_usuarios = []
            print(error)
            return lista_usuarios
    
    def excluirUsuario(self,id):
        try:
            retorno ={}
            sql = """DELETE FROM usuario WHERE usuarioid=%s"""
            values =(id,)
            excluir = self._db.update_sql(sql=sql, values=values)
            if excluir:
                retorno['Autorizado'] = True
            else:
                retorno['Autorizado']= False
            return retorno
        except Exception as error:
            print(error)
            retorno['Autorizado']= False
            return retorno
    
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
    
    def desativarUsuario(self,id):
        try:
            retorno = {}
            sql = """UPDATE usuario SET ativo=0 WHERE usuarioid =%s;"""
            values= (id,)
            upd = self._db.update_sql(sql,values)
            if upd:
                retorno['Autorizado'] = True
                return retorno
        except Exception as error:
            print("Error %s  \n Rastreio %s", error, exec())
            retorno['Autorizado'] = False
            return retorno
        
    def ativarUsuario(self,id):
        try:
            retorno = {}
            sql = """UPDATE usuario SET ativo=1 WHERE usuarioid =%s;"""
            values= (id,)
            upd = self._db.update_sql(sql,values)
            if upd:
                retorno['Autorizado'] = True
                return retorno
        except Exception as error:
            print("Error %s  \n Rastreio %s", error, exec())
            retorno['Autorizado'] = False
            return retorno
        
    def ObterPerfil(self):
        try:
            sql="""SELECT perfilId, perfil FROM public.perfil;"""
            perfil = self._db.execute_sql(sql=sql)
            return perfil
        except Exception as error:
            print(error)
            perfil =[]
            return perfil
        

        
       