from threading import Lock

from estruturas.lista_encadeada import ListaEncadeada, ListaException
from entidades.Usuario import Usuario

lock = Lock()

class Controle_usuario:
    '''
    Classe responsável por controlar as ações relativas ao usuario.
    '''
    def __init__(self, lock, lista_de_clientes):
        pass

    def registrar_cliente(self, login: str, senha: str) -> bool:
        '''
        Função responsável pela lógica de registrar o usuário no sistema.

        Retorna "True" se conseguiu registrar com sucesso.
        Retorna "False" se não foi possível registrar o usuário por já existir
        outro usuário com mesmo "login".
        '''
        with lock:
            try:
                lista_de_clientes.busca(login)
                return False
            except ListaException:
                novo_usuario = f'{login}:{senha}\n'

                arq_usuarios = open('./app/usuarios.txt', 'a')
                arq_usuarios.write(novo_usuario)
                arq_usuarios.close()

                novo_usuario = Usuario(login, senha)
                lista_de_clientes.append(novo_usuario)

                return True

    def login_cliente(self, usuario: str, senha: str) -> bool:
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

                if usuario.senha != senha:
                    raise SenhaIncorretaException()

                return True
            except ListaException:
                raise UsuarioInexistenteException()


    def deslogar(self):
        '''
        Método para deslogar um usuário do hotel.
        '''
        pass