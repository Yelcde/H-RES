from estruturas.avl import AVL
from entidades.Quarto import Quarto

class Repositorio_Quartos():
    def __init__(self):
        self.__quartos = AVL()

        self.__carregar_quartos() # Carrega os dados do arquivo "quartos.txt"

    def buscar(self, numero_quarto: int) -> Quarto:
        return self.__quartos.busca(numero_quarto)

    def tamanho(self) -> int:
        return self.tamanho()

    def __carregar_quartos(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de
        carregar os quartos salvos no arquivo "quartos.txt" na AVL do Hotel.
        '''
        arq_quartos = open('./app/quartos.txt')
        quartos = arq_quartos.readlines()[1:] # remover cabeçalho do arquivo

        for quarto in quartos:
            quarto = quarto[:-1] # remove o \n do final
            quarto = quarto.split(':')

            numero = int(quarto[0])
            tamanho = float(quarto[1])
            disponivel = bool(quarto[2])
            valor_diaria = float(quarto[3])

            quarto = Quarto(numero, tamanho, disponivel, valor_diaria)
            self.__quartos.inserir(quarto)

        arq_quartos.close()
