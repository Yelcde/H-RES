from entidades.Quarto import Quarto
from estruturas.avl import AVL
from comandos_hotel.listar import listar

class Controle_quartos:
    '''
    Classe responsável por controlar as ações relativas ao hotel.
    '''
    def __init__(self, lock, lista_de_quartos):
        self.__quartos = AVL()
        self.__quartos_ocupados = AVL()
        self.__carregar_quartos()


    def reservar(self, usuario:str, quarto: int, checkin: str, checkout: str):
        '''
        Método para reservar um quarto disponiveis dentro do hotel.

        '''
        pass


    def procurar_quarto_preco(self):
        '''
        Método para procurar um quarto por seu preço.

        '''
        pass


    def procurar_quarto_numero(self):
        '''
        Método para procurar um quarto por seu numero de identificação.

        '''
        pass


    def listar_quartos(self) -> str:
        '''
        Método para listar todos os quartos do hotel.
        '''
        return listar(self.__quartos)

    
    def __carregar_quartos(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de carregar os quartos salvos no arquivo "quartos.txt" na AVL do Hotel.
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