class Usuario:
    def __init__(self, login: str, senha: str):
        self.__login = login
        self.__senha = senha

    @property
    def login(self) -> str:
        return self.__login

    @property
    def senha(self) -> str:
        return self.__senha

    def __str__(self) -> str:
        return f'Login: {self.__login}'

    def __eq__(self, login: str) -> bool:
        return self.__login == login
