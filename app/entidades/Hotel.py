from comandos_usuario.login import login
from comandos_usuario.registrar import registrar

from entidades.Usuario import Usuario
from entidades.Quarto import Quarto

from estruturas.avl import AVL
from estruturas.lista_encadeada import ListaEncadeada

class Hotel:
    '''
    Classe responsável por lidar com ações relativas ao hotel.
    '''
    def __init__(self):
        self.__quartos = AVL()
        self.__quartos_ocupados = AVL()
        self.__clientes = ListaEncadeada()

        self.__carregar_usuarios()
        self.__carregar_quartos()

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

    def deslogar(self):
        '''
        Método para deslogar um usuário do hotel.
        '''
        pass

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
        pass

    def __carregar_usuarios(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de carregar os usuário salvos no arquivo "usuarios.txt" na lista encadeada do Hotel.
        '''
        arq_usuarios = open('./app/usuarios.txt')

        usuarios = arq_usuarios.readlines()

        for usuario_atual in usuarios:
            login, senha = usuario_atual.split(':')
            usuario_senha = senha[:-1] # remove o \n do final da string
            usuario = Usuario(login, usuario_senha)
            self.__clientes.append(usuario)

        arq_usuarios.close()

    def __carregar_quartos(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de carregar os quartos salvos no arquivo "quartos.txt" na AVL do Hotel.
        '''

        arq_quartos = open('./app/quartos.txt')
        quartos = arq_quartos.readlines()[1:] # remover cabeçalho do arquivo

        for quarto in quartos:
            quarto = quarto[:-1] # remove o \n do final
            quarto = quarto.split(':')

            numero = int(quarto[0])
            tamanho = float(quarto[1])
            disponivel = bool(quarto[2])
            valor_diaria = float(quarto[3])

            quarto = Quarto(numero, tamanho, disponivel, valor_diaria)
            self.__quartos.inserir(quarto)

        arq_quartos.close()
