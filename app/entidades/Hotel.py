from estruturas.avl import AVL

class Hotel:
    def __init__(self):
        self.__quartos_disponiveis = AVL()
        self.__quartos_ocupados = AVL()
        self.__clientes = []

    def reserva(self, id_quarto, checkin, chekout):
        pass
