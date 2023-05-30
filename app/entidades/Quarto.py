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