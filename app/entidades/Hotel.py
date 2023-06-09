from threading import Lock

from entidades.Controle_Quartos import Controle_Quartos
from entidades.Controle_Clientes import Controle_Clientes
from entidades.Repositorio_Clientes import Repositorio_Clientes
from entidades.Repositorio_Reservas import Repositorio_Reservas
from entidades.Repositorio_Quartos import Repositorio_Quartos

class Hotel:
    '''
    Classe responsável por lidar com ações relativas ao hotel.
    '''
    def __init__(self):
        repositorio_clientes = Repositorio_Clientes()
        repositorio_quartos = Repositorio_Quartos()
        repositorio_reservas = Repositorio_Reservas()

        self.__lock_clientes = Lock()
        self.__lock_quartos = Lock()
        self.__controle_clientes = Controle_Clientes(repositorio_clientes)
        self.__controle_quartos = Controle_Quartos(repositorio_quartos, repositorio_clientes, repositorio_reservas)

    # Comandos referente ao Controle de Usuario
    def registrar_cliente(self, usuario: str, senha: str) -> bool:
        '''
        Método para registrar os usuários dentro do hotel.
        '''
        return self.__controle_clientes.registrar(self.__lock_clientes, usuario, senha)

    def login_cliente(self, usuario: str, senha: str) -> bool:
        '''
        Método para realizar o login do usuário no sistema.
        '''
        return self.__controle_clientes.login(self.__lock_clientes, usuario, senha)

    # Comandos referente ao Controle do Hotel
    def reservar_quarto(self, numero_quarto: int, nome_usuario: str, checkin: str, checkout: str):
        '''
        Método para reservar um quarto
        '''
        return self.__controle_quartos.reservar(self.__lock_quartos, self.__lock_clientes, numero_quarto, nome_usuario, checkin, checkout)

    def listar_quartos_preco(self, preco_max: float):
        '''
        Método para listar os quartos com valor da diária abaixo do preço informado.
        '''
        return self.__controle_quartos.listar_quartos_preco(self.__lock_quartos, preco_max)

    def procurar_quarto_numero(self, numero_quarto: int):
        '''
        Método para procurar um quarto por seu numero de identificação.
        '''
        return self.__controle_quartos.procurar_quarto_numero(self.__lock_quartos, numero_quarto)

    def listar_quartos(self) -> str:
        '''
        Método para listar todos os quartos do hotel.
        '''
        return self.__controle_quartos.listar_quartos(self.__lock_quartos)

    def cancelar_reserva(self, numero_quarto, nome_usuario):
        ''' Método para cancelar uma reseva de quartos do hotel. '''
        return self.__controle_quartos.cancelar_reserva(self.__lock_quartos, numero_quarto, nome_usuario)
