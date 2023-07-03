import socket
import sys

HOST = 'localhost'
PORTA = 50000
TAM_MSG = 1024
LOGADO = False
NOME_USUARIO = ''

# Obter parâmetros de conexão (HOST e PORTA) pelo terminal caso seja informado
if len(sys.argv) == 2:
    HOST = sys.argv[1]
elif len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORTA = int(sys.argv[2])

codigos_respostas = {
    '200': 'Usuário registrado com sucesso.',
    '201': 'Usuário logado com sucesso.',
    '202': 'Usuário deslogado com sucesso.',
    '203': 'Quarto reservado com sucesso.',
    '204': 'Quarto encontrado.',
    '400': 'Comando inválido.',
    '402': 'Usuário já existe.',
    '403': 'Usuário não existe.',
    '404': 'Senha incorreta.',
    '405': 'Usuário não está logado.',
    '406': 'Usuário já está logado.',
    '407': 'Quarto inexistente.',
    '408': 'O preço precisa ser um valor positivo.',
    '409': 'Quarto indiponível.',
    '410': 'Data inválida.',
    '411': 'Formato de data inválido.',
    '412': 'Limite máximo de 5 diárias atingido.',
    '413': 'Não pode reservar para uma data daqui a 90 dias.'
}

def processa_solicitacao(socket_cliente) -> bool:
    '''
    Função para processar as solicitações do cliente ao servidor.

    A função retornará "False" para indicar que o usuário pode fazer
    outra solicitação para o servidor.
    '''
    global LOGADO
    global NOME_USUARIO

    try:
        solicitacao = input('H-RES <<< ')
    except KeyboardInterrupt:
        print('\nDesconectado...')
        return False

    if solicitacao != '':
        comando = solicitacao.split()[0].upper()

        if not LOGADO:
            if (comando == 'REGISTRAR' or comando == 'LOGIN'):
                socket_cliente.send(solicitacao.encode())
                dados = socket_cliente.recv(TAM_MSG)

                status, codigo = dados.decode().split()
                resposta = codigos_respostas[codigo]
                print(f'H-RES >>> {status} {codigo}, {resposta}\n')

                if codigo == '200' or codigo == '201':
                    LOGADO = True
                    NOME_USUARIO = solicitacao.split()[1]

            else:
                resposta = codigos_respostas['400']
                print(f'H-RES >>> -ERR 400, {resposta}\n')

        elif (LOGADO and comando == 'LOGIN') or (LOGADO and comando == 'REGISTRAR'):
            # Se o usuário estiver logado e tenta logar novamente
            resposta = codigos_respostas['406']
            print(f'H-RES >>> -ERR 406, {resposta}\n')

        elif (LOGADO and comando == 'LISTAR'):
            socket_cliente.send(solicitacao.encode())
            # decodifica a solicitação e salva numa variável em dados
            dados = socket_cliente.recv(TAM_MSG)
            # pega a lista de quartos e decodifica tirando o status, codigo
            status, codigo, lista_quartos = dados.decode().split()
            # da um split no listar quartos separando as outras strings da lista de quartos
            quartos = lista_quartos.split('/')
            # da um outro slip para separar a lista de quartos por quartos

            print()
            for quarto in quartos:
                quarto = quarto.split(',')
                disponibilidade = quarto[2]
                valor_diaria = float(quarto[3])
                if disponibilidade.strip() == 'True':
                    disponivel = '\033[1;34mDisponível\033[m'
                else:
                    disponivel = '\033[1;31mIndisponível\033[m'

                print(f'Numero = {quarto[0]}\nTamanho = {quarto[1]}m²\nStatus = {disponivel}\nDiária = \033[1;32mR${valor_diaria:.2f}\033[m\n')

        elif (LOGADO and comando == 'PROCURAR'):
            socket_cliente.send(solicitacao.encode())
            # decodifica a solicitação e salva numa variável em dados
            dados = socket_cliente.recv(TAM_MSG)
            # pega a lista de quartos e decodifica tirando o status, codigo
            status, codigo, quarto_procurado = dados.decode().split(' ')

            if (status == '-ERR'):
                resposta = codigos_respostas[codigo]
                print(f'H-RES >>> {status} {codigo} {resposta}\n')
            else:
                quarto = quarto_procurado.split(',')
                disponivel = '\033[1;34mDisponível\033[m'
                valor_diaria = float(quarto[3])

                print(f'\nNumero = {quarto[0]}\nTamanho = {quarto[1]}m²\nStatus = {disponivel}\nDiária = R$ {valor_diaria:.2f}\nQuantidade de banheiros = {quarto[4]}\nQuantidade de quartos = {quarto[5]}\n')

        elif (LOGADO and comando == 'PRECO'):
            socket_cliente.send(solicitacao.encode())
            # decodifica a solicitação e salva numa variável em dados
            dados = socket_cliente.recv(TAM_MSG)
            # pega a lista de quartos e decodifica tirando o status, codigo
            status, codigo, lista_quartos = dados.decode().split(' ')
            # da um split no listar quartos separando as outras strings da lista de quartos

            if (lista_quartos != ''):
                quartos = lista_quartos.split('/')
                # da um outro slip para separar a lista de quartos por quartos

                if (status == '-ERR'):
                    resposta = codigos_respostas['408']
                    print(f'H-RES >>> -ERR 408 {resposta}\n')
                else:
                    print()
                    for quarto in quartos:
                        quarto = quarto.split(',')
                        disponibilidade = quarto[2]
                        valor_diaria = float(quarto[3])
                        if disponibilidade.strip() == 'True':
                            disponivel = '\033[1;34mDisponível\033[m'
                        else:
                            disponivel = '\033[1;31mIndisponível\033[m'

                        print(f'Numero = {quarto[0]}\nTamanho = {quarto[1]}m²\nStatus = {disponivel}\nDiária = R$ {valor_diaria:.2f}\n')
            else:
                print(f'\nNão existe quarto abaixo de R$ {solicitacao.split()[1]:.2}\n')

        elif (LOGADO and comando == 'LOGOUT'):
            LOGADO = False
            resposta = codigos_respostas['202']
            print(f'H-RES >>> +OK 202, {resposta}\n')

        elif (LOGADO and comando == 'RESERVAR'):
            solicitacao = solicitacao.split()
            solicitacao.insert(2, NOME_USUARIO)
            solicitacao = ' '.join(solicitacao)

            socket_cliente.send(solicitacao.encode())

            dados = socket_cliente.recv(TAM_MSG)
            status, codigo = dados.decode().split()

            resposta = codigos_respostas[codigo]
            print(f'H-RES >>> {status} {codigo}, {resposta}\n')

        else:
            resposta = codigos_respostas['400']
            print(f'H-RES >>> -ERR 400, {resposta}\n')

    else:
        resposta = codigos_respostas['400']
        print(f'H-RES >>> -ERR 400, {resposta}\n')

    return True

print('=' * 39)
print('🏨 H-RES | Sistema de reservas de Hotel')
print('=' * 39, end='\n\n')

socket_servidor = (HOST, PORTA)

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(socket_servidor)

while True:
    if not processa_solicitacao(socket_cliente):
        break

socket_cliente.close()
