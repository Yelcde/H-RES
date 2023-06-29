class UsuarioInexistenteException(Exception):
    def __init__(self):
        super().__init__('O usuário não existe.')

class QuartoInexistenteException(Exception):
    def __init__(self):
        super().__init__('O quarto não existe.')

class SenhaIncorretaException(Exception):
    def __init__(self):
        super().__init__('Senha incorreta.')

class QuartoIndisponivelException(Exception):
    def __init__(self):
        super().__init__('Quarto Indisponível.')

class LoginRequerido(Exception):
    def __init__(self):
        super().__init__('É necessário está logado para realizar essa ação.')

class PrecoNegativo(Exception):
    def __init__(self):
        super().__init__('O preço precisa ser um valor positivo.')
