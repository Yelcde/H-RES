from entidades.Usuario import Usuario
from excecoes import SenhaIncorretaException, UsuarioInexistenteException


class Controle_Clientes:
    '''
    Classe responsável por controlar as ações relativas aos usuarios.
    '''
    def __init__(self, repositorio_clientes):
        self.__repositorio_clientes = repositorio_clientes

    def registrar(self, lock_clientes, login: str, senha: str) -> bool:
        '''
        Função responsável pela lógica de registrar o usuário no sistema.

        Retorna "True" se conseguiu registrar com sucesso.
        Retorna "False" se não foi possível registrar o usuário por já existir
        outro usuário com mesmo "login".
        '''
        with self.__lock_clientes:
            try:
                self.__clientes.busca(login)
                return False
            except ListaException:
                novo_usuario = f'{login}:{senha}\n'

                arq_usuarios = open('./app/usuarios.txt', 'a')
                arq_usuarios.write(novo_usuario)
                arq_usuarios.close()

                novo_usuario = Usuario(login, senha)
                self.__repositorio_clientes.salvar_cliente(novo_usuario)

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

