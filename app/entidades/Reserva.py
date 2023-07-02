class Reserva:
    def __init__(self, numero_quarto: int, nome_usuario: str, checkin: str, checkout: str):
        self.__numero_quarto  = numero_quarto
        self.__nome_usuario  = nome_usuario
        self.__checkin  = checkin
        self.__checkout  = checkout

    @property
    def numero_quarto (self) -> int:
        '''
        Método para ter acesso ao número do quarto reservado.
        '''
        return self.__numero_quarto

    @property
    def nome_usuario (self) -> str:
        '''
        Método para ter acesso ao usuário que solicitou a reserva.
        '''
        return self.__nome_usuario

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

    def __eq__(self, numero_quarto: int) -> bool:
        return self.__numero_quarto == numero_quarto

    def __lt__(self, numero_quarto: int) -> bool:
        return self.__numero_quarto < numero_quarto

    def __gt__(self, numero_quarto: int) -> bool:
        return self.__numero_quarto > numero_quarto
