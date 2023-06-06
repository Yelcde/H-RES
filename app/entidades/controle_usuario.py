from estruturas.lista_encadeada import ListaEncadeada, ListaException
from excecoes import UsuarioInexistenteException, SenhaIncorretaException
from entidades.Usuario import Usuario


class Controle_usuario:
    '''
    Classe responsável por controlar as ações relativas ao usuario.
    '''
    def __init__(self, lock):
        self.__clientes = ListaEncadeada()
        self.__lock = lock
        self.__carregar_usuarios()

    def registrar(self, login: str, senha: str) -> bool:
        '''
        Função responsável pela lógica de registrar o usuário no sistema.

        Retorna "True" se conseguiu registrar com sucesso.
        Retorna "False" se não foi possível registrar o usuário por já existir
        outro usuário com mesmo "login".
        '''
        with self.__lock:
            try:
                self.__clientes.busca(login)
                return False
            except ListaException:
                novo_usuario = f'{login}:{senha}\n'

                arq_usuarios = open('./app/usuarios.txt', 'a')
                arq_usuarios.write(novo_usuario)
                arq_usuarios.close()

                novo_usuario = Usuario(login, senha)
                self.__clientes.append(novo_usuario)

                return True

    def login(self, usuario: str, senha: str) -> bool:
        """
        Função responsável por realizar o login do usuário no sistema.

        Retorna "True" se conseguiu realizar o login com sucesso.

        Se o usuário não existir será lançada a exceção "UsuarioInexistenteException".
        Se a senha estiver incorreta será lançada a exceção "SenhaIncorretaException".
        """
        with self.__lock:
            try:
                posicao = self.__clientes.busca(usuario)
                usuario =  self.__clientes.elemento(posicao)

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

    def __carregar_usuarios(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de carregar os usuário salvos no arquivo "usuarios.txt" na lista encadeada do Hotel.
        '''
        arq_usuarios = open('./app/usuarios.txt')

        usuarios = arq_usuarios.readlines()

        for usuario_atual in usuarios:
            login, senha = usuario_atual.split(':')
            usuario_senha = senha[:-1] # remove o \n do final da string
            usuario = Usuario(login, usuario_senha)
            self.__clientes.append(usuario)

        arq_usuarios.close()