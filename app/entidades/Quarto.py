class Quarto:
    def __init__(
        self,
        numero: int,
        qtd_quartos: int = 2,
        qtd_banheiros: int = 2,
        tamanho: float = 12,
        preco_diaria: float = 30
    ):
        self.__numero = numero
        self.__qtd_quartos = qtd_quartos
        self.__qtd_banheiros = qtd_banheiros
        self.__tamanho = tamanho
        self.__preco_diaria = preco_diaria

    @property
    def numero (self) -> int:
        '''
        Método para ter acesso ao número do quarto do hotel.
        
        '''
        return self.__numero

    @property
    def quantidade_quartos (self) -> int:
        '''
        Método para ter acesso à quantidade de quartos no quarto.
        
        '''
        return self.__qtd_quartos

    @property
    def quantidade_banheiros (self) -> int:
        '''
        Método para ter acesso à quantidade de banheiros no quarto.
        
        '''
        return self.__qtd_banheiros
    
    @property
    def tamanho (self) -> int:
        '''
        Método para ter acesso ao tamanho geral do quarto.
        
        '''
        return self.__tamanho
    
    @property
    def preco_diaria (self) -> int:
        '''
        Método para ter acesso ao preço do quarto por diária.
        
        '''
        return self.__preco_diaria
    
    def __str__(self) -> str:
        '''
        Método para imprimir as informações do quarto para um cliente.

        '''
        return f"Número: {self.__numero} | Qtd. de quartos: {self.__qtd_quartos} | Qtd. de banheiros: {self.__qtd_banheiros} | Tamanho: {self.__tamanho} | Preço diária: {self.__preco_diaria}"