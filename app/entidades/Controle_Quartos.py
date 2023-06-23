from threading import Lock

from entidades.Quarto import Quarto
from estruturas.avl import AVL
from excecoes import QuartoIndisponivel, QuartoInexistenteException, PrecoNegativo

class Controle_Quartos:
    '''
    Classe responsável por controlar as ações relativas aos quartos.
    '''
    def __init__(self):
        self.__lock = Lock()
        self.__quartos = AVL()
        self.__quartos_ocupados = AVL()

        self.__carregar_quartos()

    def reservar(self, usuario:str, quarto: int, checkin: str, checkout: str):
        '''
        Método para reservar um quarto disponiveis dentro do hotel.
        '''
        pass

    def procurar_quarto_preco(self, preco) -> any:
        '''
        Método para procurar um quarto por seu preço.
        '''
    
        with self.__lock:
            
            assert preco > 0
            quartos = ''
            for i in range(1, len(self.__quartos) + 1):
                no = self.__quartos.busca(i)
                quarto = no.carga
                if quarto.valor_diaria <= preco:
                    disponivel = int(quarto.disponivel) # 0 -> False, 1 -> True
                    quartos += f'[{quarto.numero},{quarto.tamanho},{disponivel},{quarto.valor_diaria}]'
            return quartos

        

    def procurar_quarto_numero(self, numero_quarto) -> any:
        '''
        Método para procurar um quarto por seu numero de identificação.
        '''
        for i in range(1, len(self.__quartos) + 1):
            if quarto.numero == numero_quarto:
                if quarto.disponivel is True:
                    return quarto
                raise QuartoIndisponivel()
            no = self.__quartos.busca(i)
            quarto = no.carga
            
        raise QuartoInexistenteException()

    def listar_quartos(self) -> str:
        '''
        Função responsável por fazer a listagem de todos os quartos do hotel.

        Irá retornar uma string de quartos. Cada quarto terá suas informações agrupadas
        por colchetes ([]). Cada informação será separada por vírgula (,).
        '''
        with self.__lock:
            quartos = ''

            for i in range(1, len(self.__quartos) + 1):
                no = self.__quartos.busca(i)
                quarto = no.carga

                disponivel = int(quarto.disponivel) # 0 -> False, 1 -> True
                quartos += f'[{quarto.numero},{quarto.tamanho},{disponivel},{quarto.valor_diaria}]'

            return quartos

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
