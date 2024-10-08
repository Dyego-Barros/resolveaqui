from abc import ABC, abstractmethod

class IProduto(ABC):

    @abstractmethod
    def cadastrarProduto(self):
        pass

    @abstractmethod
    def editarProduto(self):
        pass

    @abstractmethod
    def listarProduto(self):
        pass

    @abstractmethod
    def excluirProduto(self):
        pass

    @abstractmethod
    def obterProduto(self):
        pass