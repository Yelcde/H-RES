from entidades.Usuario import Usuario
from entidades.Repositorio_Clientes import Repositorio_Clientes
from estruturas.lista_encadeada import ListaException
from excecoes import *
class Controle_Clientes:
    '''
    Classe responsável por controlar as ações relativas aos usuarios.
    '''
    def __init__(self, repositorio_clientes: Repositorio_Clientes):
        self.__repositorio_clientes = repositorio_clientes

    def registrar(self, lock_clientes, nome: str, senha: str) -> bool:
        '''
        Função responsável pela lógica de registrar o usuário no sistema.

        Retorna "True" se conseguiu registrar com sucesso.
        Retorna "False" se não foi possível registrar o usuário por já existir
        outro usuário com mesmo "nome".
        '''
        with lock_clientes:
            try:
                self.__repositorio_clientes.buscar_por_nome(nome)
                return False
            except ListaException:
                novo_usuario = f'{nome}:{senha}\n'

                arq_usuarios = open('./app/usuarios.txt', 'a')
                arq_usuarios.write(novo_usuario)
                arq_usuarios.close()

                novo_usuario = Usuario(nome, senha)
                self.__repositorio_clientes.salvar(novo_usuario)

                return True

    def login(self, lock_clientes, usuario: str, senha: str) -> bool:
        '''
        Função responsável por realizar o login do usuário no sistema.

        Retorna "True" se conseguiu realizar o login com sucesso.

        Se o usuário não existir será lançada a exceção "UsuarioInexistenteException".
        Se a senha estiver incorreta será lançada a exceção "SenhaIncorretaException".
        '''
        with lock_clientes:
            try:
                posicao = self.__repositorio_clientes.buscar_por_nome(usuario)
                usuario =  self.__repositorio_clientes.buscar_por_posicao(posicao)

                if usuario.senha != senha:
                    raise SenhaIncorretaException()

                return True
            except ListaException:
                raise UsuarioInexistenteException()
