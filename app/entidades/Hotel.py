from estruturas.avl import AVLTree

# Instanciando AVL
avl = AVLTree()

# Criando a Classe Hotel
class Hotel:
    def __init__(self):
        self.__quartos_disponiveis = None # linkar com a estrutura AVL
        self.__quartos_ocupados = None # linkar com a estrutura AVL
        self.__clientes = [] 

    def reserva(self, id_quarto, checkin, chekout):
        novareserva = Reserva(quarto, usuario, '12/03', '22/03')