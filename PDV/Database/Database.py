import psycopg2
from psycopg2.extras import RealDictCursor
from traceback import format_exc as exec
class Database():

    def __init__(self):
        self.conn()

    def conn(self):
        try:
            return psycopg2.connect(database="Pdv", user="postgres", password="postgres", host="localhost")
        
        except Exception as error:
            print(f"Error : {error} \n Rastreio : {exec()}")

    def execute_sql(self,sql, values=None):
        try:
            cnx = self.conn()
            cursor = cnx.cursor(cursor_factory=RealDictCursor)
            cursor.execute(sql,values)
            records = cursor.fetchall()
            return records
        except Exception as error:
            records = []
            print("Error ao executar query : {%s} \n Rastreio :{%s}", error, exec())
            return records
        finally: 
            cursor.close()
            cnx.close()

    def update_sql(self,sql,values=None):
        try:
            cnx = self.conn()
            cursor = cnx.cursor()
            cursor.execute(sql,values)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except Exception as error:
            print("Error ao executar query %s \n Rastreio %s", error, exec()) 
            return False         
        