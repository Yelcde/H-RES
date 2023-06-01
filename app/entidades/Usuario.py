class Usuario:
    def __init__(self, nome: str, senha: str):
        self.__nome = nome
        self.__senha = senha

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def senha(self) -> str:
        return self.__senha
