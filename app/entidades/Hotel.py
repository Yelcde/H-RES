from entidades.Controle_quartos import Controle_quartos
from entidades.Controle_usuario import Controle_usuario

Controle_usuario = Controle_usuario()
Controle_quartos = Controle_quartos()

class Hotel:
    '''
    Classe responsável por lidar com ações relativas ao hotel.
    '''
    def __init__(self):
        pass

    # Comandos referente ao Controle de Usuario
    def registrar_cliente(self, login: str, senha: str) -> bool:
        '''
        Método para registrar os usuários dentro do hotel.
        '''
        return Controle_usuario.registrar(self.__clientes, login, senha)

    def login_cliente(self, usuario: str, senha: str) -> bool:
        '''
        Método para realizar o login do usuário no sistema.
        '''
        return Controle_usuario.login(self.__clientes, usuario, senha)

    def deslogar(self):
        '''
        Método para deslogar um usuário do hotel.
        '''
        pass

    # Comandos referente ao Controle do Hotel
    def reservar_quarto(self, usuario:str, quarto: int, checkin: str, checkout: str):
        """
        Método para reservar um quarto
        """
        return Controle_quartos.reservar(usuario, quarto, checkin, checkout)

    def procurar_quarto_preco(self):
        '''
        Método para procurar um quarto por seu preço.
        '''
        return Controle_quartos.procurar_quarto_preco()

    def procurar_quarto_numero(self):
        '''
        Método para procurar um quarto por seu numero de identificação.
        '''
        return Controle_quartos.procurar_quarto_numero()

    def listar_quartos(self) -> str:
        '''
        Método para listar todos os quartos do hotel.
        '''
        return Controle_quartos.listar_quartos()