from entidades.Repositorio_Clientes import Repositorio_Clientes
from entidades.Repositorio_Quartos import Repositorio_Quartos
from estruturas.lista_encadeada import ListaException
from excecoes import PrecoNegativo, QuartoIndisponivelException, QuartoInexistenteException, UsuarioInexistenteException

class Controle_Quartos:
    '''
    Classe responsável por controlar as ações relativas aos quartos.
    '''
    def __init__(self, repositorio_quartos: Repositorio_Quartos, repositorio_clientes: Repositorio_Clientes):
        self.__repositorio_clientes = repositorio_clientes
        self.__repositorio_quartos = repositorio_quartos

    def reservar(self, lock_quartos, lock_clientes, nome_usuario: str, numero_quarto: int, checkin: str, checkout: str):
        '''
        Método para reservar um quarto disponiveis dentro do hotel.
        '''
        with lock_quartos:
            with lock_clientes:
                try:
                    self.__repositorio_clientes.buscar_por_nome(nome_usuario)

                    quarto = self.__repositorio_quartos.buscar(numero_quarto)

                    if (quarto is None):
                        raise QuartoInexistenteException()

                    if (not quarto.disponivel):
                        raise QuartoIndisponivelException()

                    # Validar datas
                except ListaException:
                    raise UsuarioInexistenteException()



    def listar_quartos_preco(self, lock_quartos, preco_max: float) -> str:
        '''
        Método para listar os quartos com valor da diária
        abaixo do preço informado.
        '''
        with lock_quartos:
            if (preco_max > 0):
                raise PrecoNegativo()

            quartos = ''

            for numero_quarto in range(1, self.__repositorio_quartos.tamanho() + 1):
                quarto = self.__repositorio_quartos.buscar(numero_quarto)

                if quarto.valor_diaria <= preco_max:
                    quartos += f'[{quarto.numero},{quarto.tamanho},{quarto.disponivel},{quarto.valor_diaria}]'

            return quartos

    def procurar_quarto_numero(self, lock_quartos, numero_quarto: int) -> str:
        '''
        Método para procurar um quarto por seu numero de identificação.
        '''
        with lock_quartos:
            quarto = self.__repositorio_quartos.buscar(numero_quarto)

            if (quarto is None):
                raise QuartoInexistenteException()
            elif (not quarto.disponivel):
                raise QuartoIndisponivelException()

            return quarto

    def listar_quartos(self, lock_quartos) -> str:
        '''
        Função responsável por fazer a listagem de todos os quartos do hotel.

        Irá retornar uma string de quartos. Cada quarto terá suas informações agrupadas
        por colchetes (/). Cada informação será separada por vírgula (,).
        '''
        with lock_quartos:
            quartos = ''

            for numero_quarto in range(1, self.__repositorio_quartos.tamanho() + 1):
                quarto = self.__repositorio_quartos.buscar(numero_quarto)
                quartos += f' ID = {quarto.numero}, TAMANHO ={quarto.tamanho} m², DISPONIVEL {quarto.disponivel}, DIARIA = {quarto.valor_diaria}/'
            return quartos
