from threading import Lock

from estruturas.lista_encadeada import ListaEncadeada, ListaException

lock = Lock()

def registrar(lista_de_clientes: ListaEncadeada, login: str, senha: str) -> bool:
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

            return True
