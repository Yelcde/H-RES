from datetime import date

from entidades.Reserva import Reserva
from entidades.Repositorio_Clientes import Repositorio_Clientes
from entidades.Repositorio_Reservas import Repositorio_Reservas
from entidades.Repositorio_Quartos import Repositorio_Quartos
from estruturas.lista_encadeada import ListaException
from excecoes import *

class Controle_Quartos:
    '''
    Classe responsável por controlar as ações relativas aos quartos.
    '''
    def __init__(
        self,
        repositorio_quartos: Repositorio_Quartos,
        repositorio_clientes: Repositorio_Clientes,
        repositorio_reservas: Repositorio_Reservas
    ):
        self.__repositorio_clientes = repositorio_clientes
        self.__repositorio_quartos = repositorio_quartos
        self.__repositorio_reservas = repositorio_reservas

    def __validar_datas_para_reserva(self, checkin: str, checkout: str):
        try:
            dia_checkin, mes_checkin, ano_checkin = [ int(x) for x in checkin.split('/') ]
            dia_checkout, mes_checkout, ano_checkout = [ int(x) for x in checkout.split('/') ]

            try:
                data_checkin = date(day=dia_checkin, month=mes_checkin, year=ano_checkin)
                data_checkout = date(day=dia_checkout, month=mes_checkout, year=ano_checkout)
                data_hoje = date.today()

                if (data_checkout < data_checkin):
                    raise DataInvalidaException()

                elif (data_checkin < data_hoje):
                    raise DataInvalidaException()

                qtd_diarias = (data_checkout - data_checkin).days + 1

                if (qtd_diarias > 5):
                    raise LimiteDiariasException()

                dias_ate_data_checkin = (data_checkin - data_hoje).days

                if (dias_ate_data_checkin > 90):
                    raise LimiteDataFuturaException()

            except ValueError:
                raise DataInvalidaException()
        except ValueError:
            raise FormatoDataInvalidoException()

    def reservar(
        self,
        lock_quartos,
        lock_clientes,
        numero_quarto: int,
        nome_usuario: str,
        checkin: str,
        checkout: str
    ):
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

                    self.__validar_datas_para_reserva(checkin, checkout)
                    self.__repositorio_quartos.atualizar_disponibilidade(numero_quarto)

                    nova_reserva = f'{numero_quarto}:{nome_usuario}:{checkin}:{checkout}\n'

                    arq_reservas = open('./app/reservas.txt', 'a')
                    arq_reservas.write(nova_reserva)
                    arq_reservas.close()

                    nova_reserva = Reserva(numero_quarto, nome_usuario, checkin, checkout)
                    self.__repositorio_reservas.salvar(nova_reserva)
                    return

                except ListaException:
                    raise UsuarioInexistenteException()

    def listar_quartos_preco(self, lock_quartos, preco_max: float) -> str:
        '''
        Método para listar os quartos com valor da diária abaixo do preço informado.
        '''
        with lock_quartos:
            if (preco_max < 0):
                raise PrecoNegativo()

            quartos = ''

            for numero_quarto in range(1, self.__repositorio_quartos.tamanho() + 1):
                quarto = self.__repositorio_quartos.buscar(numero_quarto)

                if quarto.valor_diaria <= preco_max:
                    quartos += f'{quarto.numero},{quarto.tamanho},{quarto.disponivel},{quarto.valor_diaria}/'

            return quartos

    def procurar_quarto_numero(self, lock_quartos, numero_quarto: int) -> str:
        '''
        Método para procurar um quarto por seu numero de identificação.
        Irá retornar uma string do quarto selecionado. O quarto terá suas informações agrupadas
        por colchetes (/). Cada informação será separada por vírgula (,).
        '''
        with lock_quartos:
            quarto = self.__repositorio_quartos.buscar(numero_quarto)
            quarto_procurado += f'{quarto.numero},{quarto.tamanho},{quarto.disponivel},{quarto.valor_diaria}/'

            if (quarto is None):
                raise QuartoInexistenteException()
            elif (not quarto.disponivel):
                raise QuartoIndisponivelException()

            return quarto_procurado

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
                quartos += f'{quarto.numero},{quarto.tamanho},{quarto.disponivel},{quarto.valor_diaria}/'
            return quartos
