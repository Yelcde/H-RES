from Quarto import Quarto
from Usuario import Usuario

class Reserva:
    def __init__(self, quarto: Quarto, usuario: Usuario, checkin: str, checkout: str):
        self.__quarto  = quarto
        self.__usuario  = usuario
        self.__checkin  = checkin
        self.__checkout  = checkout

    @property
    def quarto (self) -> 'quarto':
        '''
        Método para ter acesso ao número do quarto reservado.
        
        '''
        return self.__quarto
    
    @property
    def usuario (self) -> 'usuario':
        '''
        Método para ter acesso ao usuário que solicitou a reserva.
        
        '''
        return self.__usuario

    @property
    def checkin (self) -> str:
        '''
        Método para ter acesso ao checkin feito na reserva.
        
        '''
        return self.__checkin

    @property
    def checkout (self) -> str:
        '''
        Método para ter acesso ao checkout feito na reserva.
        
        '''
        return self.__checkout
    
    def __eq__(self, usuario: str) -> bool:
        return self.__usuario == usuario
    
    def __str__(self) -> str:
        '''
        Método para imprimir as informações da reserva de um quarto.

        '''
        return f"Quarto: {self.__quarto}\nUsuário: {self.__usuario}\nCheck-in: {self.__checkin}\nCheck-out: {self.__checkout}"