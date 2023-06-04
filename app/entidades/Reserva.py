from Quarto import Quarto
from Usuario import Usuario

class Reserva:
    def __init__(self, quarto: Quarto, usuario: Usuario, checkin: str, checkout: str):
        self.__quarto  = quarto
        self.__usuario  = usuario
        self.__checkin  = checkin
        self.__checkout  = checkout

    @property
    def quarto (self) -> int:
        '''
        Método para ter acesso ao número do quarto do hotel.
        
        '''
        return self.__numero
    
    @property
    def quarto (self) -> int:
        '''
        Método para ter acesso ao número do quarto do hotel.
        
        '''
        return self.__numero

    @property
    def checkin (self) -> int:
        '''
        Método para ter acesso à quantidade de quartos no quarto.
        
        '''
        return self.__qtd_quartos

    @property
    def checkout (self) -> int:
        '''
        Método para ter acesso à quantidade de banheiros no quarto.
        
        '''
        return self.__qtd_banheiros
    