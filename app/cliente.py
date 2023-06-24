import socket
import sys

HOST = 'localhost'
PORTA = 50000
TAM_MSG = 1024
LOGADO = False

# Obter parâmetros de conexão (HOST e PORTA) pelo terminal caso seja informado
if len(sys.argv) == 2:
    HOST = sys.argv[1]
elif len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORTA = int(sys.argv[2])

codigos_respostas = {
    '200': 'Usuário registrado com sucesso.',
    '201': 'Usuário logado com sucesso.',
    '202': 'Usuário deslogado com sucesso',
    '207': 'Lista acessada',
    '211': 'Quarto encontrado',
    '400': 'Comando inválido.',
    '402': 'Usuário já existe.',
    '403': 'Usuário não existe.',
    '404': 'Senha incorreta.',
    '411': 'Usuário não está logado.',
    '412': 'Usuário já está logado.',
    '413': 'Quarto Inexistente.',
    '414': 'O preço precisa ser um valor positivo.',
    '415': 'Quarto indiponível.'
}

def processa_solicitacao(socket_cliente) -> bool:
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
        usuario = solicitacao[1]

        if not LOGADO:
            if (comando == 'REGISTRAR' or comando == 'LOGIN'):
                socket_cliente.send(solicitacao.encode())
                dados = socket_cliente.recv(TAM_MSG)

                status, codigo = dados.decode().split()
                resposta = codigos_respostas[codigo]
                print(f'{status} {codigo}, {resposta}\n')

                if codigo == '200' or codigo == '201':
                    LOGADO = True

            else:
                resposta = codigos_respostas['411']
                print(f'-ERR 411, {resposta}\n')

        elif (LOGADO and comando == 'LOGIN') or (LOGADO and comando == 'REGISTRAR'):
            # Se o usuário estiver logado e tenta logar novamente
            resposta = codigos_respostas['412']
            print(f'-ERR 412, {resposta}\n')

        elif (LOGADO and comando == 'LOGOUT'):
            LOGADO = False
            resposta = codigos_respostas['202']
            print(f'+OK 202, {resposta}\n')

        # se tiver logado, envia a solicitacao ao servidor
        else:
            solicitacao += ' ' + usuario # envia para o servidor com o seu usuario marcando que é ele.
            socket_cliente.send(solicitacao.encode()) # envia a solicitacao ao servidor com seu registro

            # recebe a solicitação enviada pelo serividor
            dados = socket_cliente.recv(TAM_MSG)
            dados = dados.decode() # decodifica a mensagem enviada pelo servidor
            print(dados) # printa a mensagem enviada pelo servidor

            # procurar no codigos resposta a mensagem decodificada pelo enviada pelo serividor
            status, codigo = dados.decode().split()
            resposta = codigos_respostas[codigo]
    else:
        resposta = codigos_respostas['400']
        print(f'-ERR 400, {resposta}\n')

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
