from abc import ABC, abstractmethod

class Iempresa(ABC):

    @abstractmethod
    def cadastrar_empresa(self):
        pass
    
    @abstractmethod
    def editar_empresa(self):
        pass

    @abstractmethod
    def excluir_empresa(self):
        pass

    @abstractmethod
    def ativar_empresa(self):
        pass

    @abstractmethod
    def desativar_empresa(self):
        pass