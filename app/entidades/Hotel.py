from comandos_usuario.login import login
from comandos_usuario.registrar import registrar
from comandos_hotel import listar_quarto
from entidades.Usuario import Usuario
from entidades.Quarto import *
from comandos_usuario import logout
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
        '''
        Método para registrar os usuários dentro do hotel.
        '''
        return registrar(self.__clientes, login, senha)

    def login_cliente(self, usuario: str, senha: str) -> bool:
        '''
        Método para realizar o login do usuário no sistema.
        '''
        return login(self.__clientes, usuario, senha)

    def __carregar_usuarios(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de carregar os usuário salvos no arquivo "usuarios.txt" na lista encadeada do Hotel.
        '''
        arq_usuarios = open('./app/usuarios.txt')

        usuarios = arq_usuarios.readlines()

        for usuario_atual in usuarios:
            login, senha = usuario_atual.split(':')
            usuario = Usuario(login, senha)
            self.__clientes.append(usuario)

        arq_usuarios.close()

    def deslogar(self)-> bool:
        '''
        Método para deslogar um usuário do hotel.

        '''
        return logout()


    def reservar(self, usuario:str, quarto: int, checkin: str, checkout: str):
        '''
        Método para reservar um quarto disponiveis dentro do hotel.

        '''
        pass

    def procurar_quarto_preco(self):
        '''
        Método para procurar um quarto por seu preço.

        '''
        pass

    def procurar_quarto_numero(self):
        '''
        Método para procurar um quarto por seu numero de identificação.

        '''
        pass

    def listar_quartos_disponiveis(self) -> str:
        '''
        Método para listar todos os quartos disponiveis dentro do hotel.

        '''
        return listar_quarto(self.__quartos_disponiveis)
