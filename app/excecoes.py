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

class DataInvalidaException(Exception):
    def __init__(self):
        super().__init__('Data inválida.')

class LimiteDiariasException(Exception):
    def __init__(self):
        super().__init__('Limite máximo de diárias atingindo (5).')

class LimiteDataFuturaException(Exception):
    def __init__(self):
        super().__init__('Limite de dias de reserva de quarto no futuro atingido (90 dias).')

class FormatoDataInvalidoException(Exception):
    def __init__(self):
        super().__init__('Formato de data inválido, informe DIA/MES/ANO.')

class ReservaInexistente(Exception):
    def __init__(self):
        super().__init__('Essa reserva não existe.')
