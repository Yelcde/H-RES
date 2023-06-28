from estruturas.lista_encadeada import ListaEncadeada


class Repositorio_Clientes():
    def __init__(self) -> None:
        self.__clientes = ListaEncadeada()

        self.__carregar_clientes() # Carrega os dados do arquivo "usuarios.txt"


    def salvar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def __carregar_clientes(self):
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
