from entidades.Controle_Quartos import Controle_Quartos
from app.entidades.Controle_Clientes import Controle_Clientes

class Hotel:
    '''
    Classe responsável por lidar com ações relativas ao hotel.
    '''
    def __init__(self):
        self.__controle_clientes = Controle_Clientes()
        self.__controle_quartos = Controle_Quartos()

    # Comandos referente ao Controle de Usuario
    def registrar_cliente(self, usuario: str, senha: str) -> bool:
        '''
        Método para registrar os usuários dentro do hotel.
        '''
        return self.__controle_clientes.registrar(usuario, senha)

    def login_cliente(self, usuario: str, senha: str) -> bool:
        '''
        Método para realizar o login do usuário no sistema.
        '''
        return self.__controle_clientes.login(usuario, senha)

    def deslogar(self):
        '''
        Método para deslogar um usuário do hotel.
        '''
        pass

    # Comandos referente ao Controle do Hotel
    def reservar_quarto(self, usuario: str, quarto: int, checkin: str, checkout: str):
        """
        Método para reservar um quarto
        """
        return self.__controle_quartos.reservar(usuario, quarto, checkin, checkout)

    def procurar_quarto_preco(self):
        '''
        Método para procurar um quarto por seu preço.
        '''
        return self.__controle_quartos.procurar_quarto_preco()

    def procurar_quarto_numero(self):
        '''
        Método para procurar um quarto por seu numero de identificação.
        '''
        return self.__controle_quartos.procurar_quarto_numero()

    def listar_quartos(self) -> str:
        '''
        Método para listar todos os quartos do hotel.
        '''
        return self.__controle_quartos.listar_quartos()
