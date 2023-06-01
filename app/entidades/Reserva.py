from Quarto import Quarto
from Usuario import Usuario

class Reserva:
    def __init__(self, quarto: Quarto, usuario: Usuario, checkin: str, checkout: str):
        self.__quarto  = quarto
        self.__usuario  = usuario
        self.__checkin  = checkin
        self.__checkout  = checkout
