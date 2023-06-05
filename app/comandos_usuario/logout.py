from threading import Lock

from estruturas.lista_encadeada import ListaException
from excecoes import LoginRequerido

lock = Lock()

def logout(is_authenticated: bool) -> bool:
    """
    Função responsável por realizar o logout do usuário.

    Retorna "True" se conseguiu sair da conta com sucesso.

    Se o usuário não estiver logado será lançada a exceção "LoginRequerido".
    """
    with lock:
        try:
            if is_authenticated is True:
                return False

        except ListaException:
            raise LoginRequerido