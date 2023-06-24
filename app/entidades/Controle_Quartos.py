from threading import Lock

from entidades.Quarto import Quarto
from estruturas.avl import AVL
from excecoes import QuartoIndisponivel, QuartoInexistenteException, PrecoNegativo

class Controle_Quartos:
    '''
    Classe responsável por controlar as ações relativas aos quartos.
    '''
    def __init__(self):
        self.__mutex_quartos = Lock()
        self.__mutex_reservas = Lock()
        self.__quartos = AVL()
        self.__reservas = AVL()

        self.__carregar_quartos()

    def reservar(self, usuario:str, quarto: int, checkin: str, checkout: str):
        '''
        Método para reservar um quarto disponiveis dentro do hotel.
        '''
        pass

    def listar_quartos_preco(self, preco_max: float) -> str:
        '''
        Método para listar os quartos com valor da diária
        abaixo do preço informado.
        '''
        with self.__mutex_quartos:
            if (preco_max > 0):
                raise PrecoNegativo()

            quartos = ''

            for i in range(1, len(self.__quartos) + 1):
                quarto = self.__quartos.busca(i).carga

                if quarto.valor_diaria <= preco_max:
                    quartos += f'[{quarto.numero},{quarto.tamanho},{quarto.disponivel},{quarto.valor_diaria}]'

            return quartos

    def procurar_quarto_numero(self, numero_quarto: int) -> str:
        '''
        Método para procurar um quarto por seu numero de identificação.
        '''
        quarto = self.__quartos.busca(numero_quarto).carga

        if (quarto is None):
            raise QuartoInexistenteException()
        elif (not quarto.disponivel):
            raise QuartoIndisponivel()

        return quarto

    def listar_quartos(self) -> str:
        '''
        Função responsável por fazer a listagem de todos os quartos do hotel.

        Irá retornar uma string de quartos. Cada quarto terá suas informações agrupadas
        por colchetes ([]). Cada informação será separada por vírgula (,).
        '''
        with self.__mutex_quartos:
            quartos = ''

            for i in range(1, len(self.__quartos) + 1):
                quarto = self.__quartos.busca(i).carga
                quartos += f'[{quarto.numero},{quarto.tamanho},{quarto.disponivel},{quarto.valor_diaria}]'

            return quartos

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
