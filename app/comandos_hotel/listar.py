from threading import Lock

from estruturas.avl import AVL

lock = Lock()

def listar(avl_quartos: AVL) -> str:
    '''
    Função responsável por fazer a listagem de todos os quartos do hotel.

    Irá retornar uma string de quartos. Cada quarto terá suas informações agrupadas
    por colchetes ([]). Cada informação será separada por vírgula (,).
    '''
    quartos = ''

    with lock:
        for i in range(1, len(avl_quartos) + 1):
            no = avl_quartos.busca(i)
            quarto = no.carga

            disponivel = int(quarto.disponivel) # 0 -> False, 1 -> True
            quartos += f'[{quarto.numero},{quarto.tamanho},{disponivel},{quarto.valor_diaria}]'

    return quartos
