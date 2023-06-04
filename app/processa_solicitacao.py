from socket import socket


TAM_MSG = 1024
LOGADO = False

codigos_respostas = {
    '200': 'Usuário registrado com sucesso.',
    '201': 'Usuário logado com sucesso.',
    '400': 'Comando inválido.',
    '402': 'Usuário já existe.',
    '403': 'Usuário não existe.',
    '410': 'Usuário já está logado.',

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
        usuario = solicitacao[1]

        if not LOGADO:
            if comando == 'REGISTRAR' or comando == 'LOGIN':
                socket_cliente.send(solicitacao.encode())
                dados = socket_cliente.recv(TAM_MSG)


                status, codigo = dados.decode().split()
                resposta = codigos_respostas[codigo]

                print(f'{status} {codigo}, {resposta}\n')


                if codigo == 200:
                    LOGADO = True
                elif codigo == 201:
                    LOGADO = True
                     

        elif LOGADO and (comando.split(' ')[0].upper() == 'LOGIN') or LOGADO and (comando.split(' ')[0].upper() == 'REGISTRAR'):
        # Se o usuário estiver logado e tenta logar dnv
            status, codigo = dados.decode().split()
            resposta = codigos_respostas[codigo]
	    
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
        print('Comando inválido.\n')

    return True
