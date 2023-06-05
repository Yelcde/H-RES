class UsuarioInexistenteException(Exception):
    def __init__(self):
        super().__init__(f'O usuário não existe.')

class SenhaIncorretaException(Exception):
    def __init__(self):
        super().__init__('Senha incorreta.')
