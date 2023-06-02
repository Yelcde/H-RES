from estruturas.lista_encadeada import ListaEncadeada
from entidades.Usuario import Usuario

def registrar(lista_clientes: ListaEncadeada, usuario: str, senha: str) -> bool:
    try:
        lista_clientes.busca(usuario)
        return False
    except:
        # lock para lidar com arquivo compartilhado "usuarios.txt"
        # lógica para registrar clientes
        # abre regiao critica
            # edita txt
        # fecha
        return True
