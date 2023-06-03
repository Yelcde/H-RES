from estruturas.avl import AVL
from comandos_usuario import registrar
from comandos_usuario import login
from comandos_hotel import listar_quarto
from estruturas.lista_encadeada import ListaEncadeada

class Hotel:
    def __init__(self):
        self.__quartos_disponiveis = AVL()
        self.__quartos_ocupados = AVL()
        self.__clientes = ListaEncadeada()

    def registrar_cliente(self, usuario, senha) -> bool:
        return registrar(self.__clientes, usuario, senha)

    def login_cliente(self, usuario, senha) -> bool:
        try:
           self.__clientes.busca(usuario)
           return self.__clientes(login(usuario, senha))
        except:
            return False
    def listar(self) -> object:
        return listar_quarto(self.__quartos_disponiveis)
