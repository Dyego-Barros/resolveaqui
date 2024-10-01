from abc import ABC, abstractmethod

class IUsuario(ABC):
    @abstractmethod
    def cadastrarUsuario(self):
        pass

    @abstractmethod
    def editarUsuario(self):
        pass

    @abstractmethod
    def listarUsuario(self):
        pass

    @abstractmethod
    def excluirUsuario(self):
        pass

    @abstractmethod
    def obterUsuario(self):
        pass

    @abstractmethod
    def loginUsuario(self):
        pass