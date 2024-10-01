from Empresas.interfaces.Iempresa import Iempresa
from Empresas.domain.entities.empresa import Empresa
from django.db import connection
import uuid6
from Database.Database import Database
from PDV.config import cripto
from cryptocode import decrypt, encrypt

class RepositorieEmpresa(Iempresa):

    def __init__(self):
        self._db = Database()

    def cadastrar_empresa(self,empresa:dict):
        try:
            retorno = {}            
            empresaid = uuid6.uuid7()#Cria o Id da empresa  
            del empresa['csrfmiddlewaretoken']          
            query ="""INSERT INTO public.empresa (empresaid,razaosocial,cnpj,nomefantasia,nome,cpf,email,telefone,ativo)
               VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
            dado = Empresa(**empresa)#Instância da classe Empresa
            dado.empresaid = str(empresaid)#Define a propriedade EmpresaId
            dado.ativo = 1#Define a propriedade Ativo            
            values = (dado.empresaid, dado.razaosocial,dado.cnpj, dado.nomefantasia,dado.nome, encrypt(dado.cpf, cripto()), dado.email, dado.telefone,dado.ativo)
            self._db.update_sql(query, values)            

           
            #Seleciona o perfil para criar o usuario padrão da empresa
            perfil_query ="""SELECT perfilid  FROM public.perfil WHERE perfil ='ADM';"""           
            perfilid = self._db.execute_sql(perfil_query)
            
            perfilid = str(perfilid[0]['perfilid'])#Obtem o perfilid para criar o usuario padrão junto a criação da empresa
            print(perfilid)
            ###Cria o usuario padrão no momento do cadastro da empresa
            usuarioId = uuid6.uuid7()
            usuarioId = str(usuarioId)#Define Usuarioid
            
            query_2 = """INSERT INTO public.usuario(usuarioid,nome,email,funcao,cargo,senha,ativo,perfilid,empresaid)
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            senha = encrypt( dado.empresaid[-8:],cripto())#Criptografa a senha do usuario no banco
            values=(usuarioId, dado.nome,dado.email,'Administrador','Administrador',senha,1,perfilid,dado.empresaid)
            self._db.update_sql(query_2, values)
           

            #Logica de enviar email pro usuario cadastrado  passando alguma informações

            retorno['Autorizado'] = True
            retorno['Mensagem'] = "Empresa cadastrada com sucesso!"
        except Exception as error:
            print(error)
            retorno['Autorizado'] = False
            retorno['Mensagem']= "Falha ao cadastrar Empresa!"
        return retorno
    

    
    def editar_empresa(self, empresa: dict):
        try:
            cursor = connection.cursor()

            query = """
            UPDATE empresa
            SET razaosocial = %s, cnpj = %s, nomefantasia = %s, nome = %s,
                cpf = %s, email = %s, telefone = %s, ativo = %s
            WHERE empresaid = %s;
            """
            values = (
                empresa.get('razaosocial'), empresa.get('cnpj'),
                empresa.get('nomefantasia'), empresa.get('nome'),
                empresa.get('cpf'), empresa.get('email'),
                empresa.get('telefone'), int(empresa.get('ativo')),
                empresa.get('empresaid')
            )

            cursor.execute(query, values)
            cursor.close()

            return {"Mensagem": "Empresa editada com sucesso!"}
        except Exception as error:
            return {"Mensagem": "Falha ao editar Empresa!", "Erro": str(error)}

    def excluir_empresa(self, empresa_id: str):
        try:
            cursor = connection.cursor()

            query = "DELETE FROM empresa WHERE empresaid = %s;"
            cursor.execute(query, [empresa_id])
            cursor.close()

            return {"Mensagem": "Empresa excluída com sucesso!"}
        except Exception as error:
            return {"Mensagem": "Falha ao excluir Empresa!", "Erro": str(error)}

    def ativar_empresa(self, empresa_id: str):
        try:
            cursor = connection.cursor()

            query = "UPDATE empresa SET ativo = 1 WHERE empresaid = %s;"
            cursor.execute(query, [empresa_id])
            cursor.close()

            return {"Mensagem": "Empresa ativada com sucesso!"}
        except Exception as error:
            return {"Mensagem": "Falha ao ativar Empresa!", "Erro": str(error)}

    def desativar_empresa(self, empresa_id: str):
        try:
            cursor = connection.cursor()

            query = "UPDATE empresa SET ativo = 0 WHERE empresaid = %s;"
            cursor.execute(query, [empresa_id])
            cursor.close()

            return {"Mensagem": "Empresa desativada com sucesso!"}
        except Exception as error:
            return {"Mensagem": "Falha ao desativar Empresa!", "Erro": str(error)}

       
      