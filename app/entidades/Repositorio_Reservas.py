from estruturas.avl import AVL
from entidades.Reserva import Reserva

class Repositorio_Reservas():
    def __init__(self):
        self.__reservas = AVL()
        self.__carregar_reservas()

    def salvar(self, reserva):
        self.__reservas.inserir(reserva)

    def __carregar_reservas(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de
        carregar as reservas salvas no arquivo "reservas.txt" na AVL do repositório.
        '''
        arq_reservas = open('./app/reservas.txt')
        reservas = arq_reservas.readlines()[1:] # remover cabeçalho do arquivo

        for reserva in reservas:
            reserva = reserva[:-1] # remove o \n do final
            reserva = reserva.split(':')

            numero_quarto = int(reserva[0])
            nome_usuario = reserva[1]
            checkin = reserva[2]
            checkout = reserva[3]

            reserva = Reserva(numero_quarto, nome_usuario, checkin, checkout)
            self.__reservas.inserir(reserva)

        arq_reservas.close()
