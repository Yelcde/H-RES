from estruturas.avl import AVL
from entidades.Quarto import Quarto

class Repositorio_Quartos():
    def __init__(self):
        self.__quartos = AVL() # Estrutura onde os quartos estão salvos
        self.__carregar_quartos() # Carrega os dados do arquivo "quartos.txt"

    def atualizar_disponibilidade(self, numero_quarto: int):
        quarto = self.buscar(numero_quarto)
        self.__quartos.remover(numero_quarto)

        if (not quarto.disponivel):
            quarto.disponivel = True
        else:
            quarto.disponivel = False

        self.__quartos.inserir(quarto)

    def buscar(self, numero_quarto: int) -> Quarto:
        return self.__quartos.busca(numero_quarto)

    def tamanho(self) -> int:
        return self.__quartos.count()

    def __carregar_quartos(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de
        carregar os quartos salvos no arquivo "quartos.txt" na AVL do repositório.
        '''
        arq_quartos = open('./app/quartos.txt')
        quartos = arq_quartos.readlines()[1:] # remover cabeçalho do arquivo

        for quarto in quartos:
            quarto = quarto[:-1] # remove o \n do final
            quarto = quarto.split(':')

            numero = int(quarto[0])
            tamanho = float(quarto[1])
            disponivel = True
            valor_diaria = float(quarto[2])

            quarto = Quarto(numero, tamanho, disponivel, valor_diaria)
            self.__quartos.inserir(quarto)

        arq_quartos.close()

        arq_reservas = open('./app/reservas.txt')
        reservas = arq_reservas.readlines()[1:] # remover cabeçalho do arquivo

        for reserva in reservas:
            reserva = reserva[:-1] # remove o \n do final
            numero_quarto = int(reserva.split(':')[0])

            self.atualizar_disponibilidade(numero_quarto)

        arq_reservas.close()
