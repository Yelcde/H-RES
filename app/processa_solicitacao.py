from socket import socket

TAM_MSG = 1024
LOGADO = False

codigos_respostas = {
    '200': 'Usuário registrado com sucesso.',
    '201': 'Usuário logado com sucesso.',
    '400': 'Comando inválido.',
    '402': 'Usuário já existe.',
    '403': ' Usuário não existe.'
}

def processa_solicitacao(socket_cliente: socket) -> bool:
    '''
    Função para processar as solicitações do cliente ao servidor.

    A função retornará "False" para indicar que o usuário pode fazer
    outra solicitação para o servidor.
    '''
    global LOGADO

    try:
        solicitacao = input('H-RES >>> ')
    except KeyboardInterrupt:
        solicitacao = 'SAIR'
        print('\nDesconectado...')
        return False

    if solicitacao != '':
        comando = solicitacao.split()[0].upper()

        if not LOGADO:
            if comando == 'REGISTRAR' or comando == 'LOGIN':
                socket_cliente.send(solicitacao.encode())
                dados = socket_cliente.recv(TAM_MSG)

                status, codigo = dados.decode().split()
                resposta = codigos_respostas[codigo]

                print(f'{status} {codigo}, {resposta}\n')

                if codigo == 201:
                    LOGADO = True
    else:
        print('Comando inválido\n')

    return True
