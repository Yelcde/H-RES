from estruturas.avl import AVL
from comandos_usuario import registrar 
from comandos_usuario import login 
from estruturas.lista_encadeada import ListaEncadeada

class Hotel:
    def __init__(self):
        self.__quartos_disponiveis = AVL()
        self.__quartos_ocupados = AVL()
        self.__clientes = ListaEncadeada()

    def registrar_cliente(self, usuario, senha):
        try:
            _ = self.__clientes.busca(usuario)
            return False
        except:
            self.__clientes.append(registrar(usuario, senha))
            return True
        
    def login_cliente(self, usuario, senha) -> bool:
        try:
            pesquisa = self.__clientes.busca(usuario)
            if pesquisa is not None: 
                return self.__cliente.pegar(login(usuario, senha))
        except:
            return False

