from comandos_usuario.login import login_usuario
from comandos_usuario.registrar import registrar
# from comandos_hotel.listar_quarto import listar_quarto
from entidades.Usuario import Usuario
from estruturas.avl import AVL
from estruturas.lista_encadeada import ListaEncadeada

class Hotel:
    '''
    Classe responsável por lidar com ações relativas ao hotel.
    '''
    def __init__(self):
        self.__quartos_disponiveis = AVL()
        self.__quartos_ocupados = AVL()
        self.__clientes = ListaEncadeada()

        self.__carregar_usuarios()

    def registrar_cliente(self, login: str, senha: str) -> bool:
        return registrar(self.__clientes, login, senha)

    def login_cliente(self, usuario, senha) -> bool:
        try:
           self.__clientes.busca(usuario)
           return self.__clientes(login_usuario(usuario, senha))
        except:
            return False

    def __carregar_usuarios(self):
        arq_usuarios = open('./app/usuarios.txt')

        usuarios = arq_usuarios.readlines()

        for usuario_atual in usuarios:
            login, senha = usuario_atual.split(':')
            usuario = Usuario(login, senha)
            self.__clientes.append(usuario)

        arq_usuarios.close()
    def listar(self) -> object:
        pass
        # return listar_quarto(self.__quartos_disponiveis)
