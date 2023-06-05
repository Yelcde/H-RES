class Usuario:
    def __init__(self, usuario: str, senha: str):
        self.__usuario = usuario
        self.__senha = senha

    @property
    def usuario(self) -> str:
        return self.__usuario

    @property
    def senha(self) -> str:
        return self.__senha

    def __str__(self) -> str:
        return f'Usuário: {self.__usuario}'

    def __eq__(self, usuario: str) -> bool:
        return self.__usuario == usuario
