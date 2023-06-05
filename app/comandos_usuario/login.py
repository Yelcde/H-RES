from threading import Lock

from estruturas.lista_encadeada import ListaEncadeada, ListaException
from excecoes import UsuarioInexistenteException, SenhaIncorretaException

lock = Lock()

def login(lista_de_usuarios: ListaEncadeada, usuario: str, senha: str) -> bool:
    """
    Função responsável por realizar o login do usuário no sistema.

    Retorna "True" se conseguiu realizar o login com sucesso.

    Se o usuário não existir será lançada a exceção "UsuarioInexistenteException".
    Se a senha estiver incorreta será lançada a exceção "SenhaIncorretaException".
    """
    with lock:
        try:
            posicao = lista_de_usuarios.busca(usuario)
            usuario = lista_de_usuarios.elemento(posicao)
            usuario_senha = usuario.senha[:-1] # remove o \n do final

            if usuario_senha != senha:
                raise SenhaIncorretaException()

            return True
        except ListaException:
            raise UsuarioInexistenteException()
