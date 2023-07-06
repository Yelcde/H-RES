from estruturas.lista_encadeada import ListaEncadeada
from entidades.Usuario import Usuario

class Repositorio_Clientes():
    '''
    Classe responsável por armazenar os clientes cadastrados.
    '''
    def __init__(self):
        self.__clientes = ListaEncadeada() # Estrutura onde os clientes estão salvos
        self.__carregar_clientes() # Carrega os dados do arquivo "usuarios.txt"

    def salvar(self, cliente: Usuario):
        self.__clientes.append(cliente)

    def buscar_por_nome(self, nome: str) -> int:
        return self.__clientes.busca(nome)

    def buscar_por_posicao(self, posicao: int) -> Usuario:
        return self.__clientes.elemento(posicao)

    def __carregar_clientes(self):
        '''
        Método usado no momento que a classe é instanciada com o propósito de carregar os usuário salvos no arquivo "usuarios.txt" na lista encadeada de clientes.
        '''
        arq_usuarios = open('./app/usuarios.txt')

        usuarios = arq_usuarios.readlines()

        for usuario_atual in usuarios:
            login, senha = usuario_atual.split(':')
            usuario_senha = senha[:-1] # remove o \n do final da string
            usuario = Usuario(login, usuario_senha)
            self.__clientes.append(usuario)

        arq_usuarios.close()
