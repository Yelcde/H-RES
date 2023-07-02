class Quarto:
    def __init__(
        self,
        numero: int,
        tamanho: float = 12,
        disponivel: bool = True,
        valor_diaria: float = 80,
        qtd_quartos: int = 2,
        qtd_banheiros: int = 2
    ):
        self.__numero = numero
        self.__tamanho = tamanho
        self.__disponivel = disponivel
        self.__valor_diaria = valor_diaria
        self.__qtd_quartos = qtd_quartos
        self.__qtd_banheiros = qtd_banheiros

    @property
    def numero(self) -> int:
        '''
        Método para ter acesso ao número do quarto do hotel.
        '''
        return self.__numero

    @property
    def quantidade_quartos(self) -> int:
        '''
        Método para ter acesso à quantidade de quartos no quarto.

        '''
        return self.__qtd_quartos

    @property
    def quantidade_banheiros(self) -> int:
        '''
        Método para ter acesso à quantidade de banheiros no quarto.

        '''
        return self.__qtd_banheiros

    @property
    def disponivel(self) -> bool:
        '''
        Método para ter acesso se o quarto está disponível.
        '''
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, status: bool):
        self.__disponivel = status

    @property
    def tamanho(self) -> str:
        '''
        Método para ter acesso ao tamanho do quarto em metro quadrado(m2).
        '''
        return f'{self.__tamanho}m2'

    @property
    def valor_diaria(self) -> str:
        '''
        Método para ter acesso ao preço do quarto por diária.
        '''
        return f'R${self.__valor_diaria:.2f}'

    def __str__(self) -> str:
        '''
        Método para imprimir as informações do quarto para um cliente.
        '''
        return f"Número: {self.__numero} | Disponível: {self.__disponivel} | Qtd. de quartos: {self.__qtd_quartos} | Qtd. de banheiros: {self.__qtd_banheiros} | Tamanho: {self.__tamanho} | Preço diária: {self.__valor_diaria}"

    def __eq__(self, numero: int) -> bool:
        return self.__numero == numero

    def __lt__(self, numero: int) -> bool:
        return self.__numero < numero

    def __gt__(self, numero: int) -> bool:
        return self.__numero > numero
