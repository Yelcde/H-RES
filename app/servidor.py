import socket
import threading

from entidades.Hotel import Hotel
from excecoes import *

TAM_MSG = 1024
HOST = 'localhost'
PORT = 50000

def atender_cliente(socket_cliente, endereco_cliente, solicitacao) -> bool:
    '''
    Função responsável por processar os dados que serão
    enviados pelo cliente para o servidor.

    Retorna "True" caso tenha conseguido processar a solicitação do usuário.
    Retorna "False" caso o usuário faça o LOGOUT na aplicação.
    '''
    solicitacao = solicitacao.decode()

    print(f'Cliente {endereco_cliente} mandou: {solicitacao}')

    solicitacao = solicitacao.split()
    comando = solicitacao[0].upper()
    resposta = ''

    if comando == 'REGISTRAR' and len(solicitacao) == 3:
        login = solicitacao[1]
        senha = solicitacao[2]

        registrou = hotel.registrar_cliente(login, senha)

        if registrou:
            resposta = str.encode('+OK 200')
        else:
            resposta = str.encode('-ERR 402')

    elif comando == 'LOGIN' and len(solicitacao) == 3:
        usuario = solicitacao[1]
        senha = solicitacao[2]

        try:
            logou = hotel.login_cliente(usuario, senha)

            if logou:
                resposta = str.encode('+OK 201')
        except UsuarioInexistenteException:
            resposta = str.encode('-ERR 403')
        except SenhaIncorretaException:
            resposta = str.encode('-ERR 404')

    elif comando == 'LOGOUT' and len(solicitacao) == 3:
        try:
            hotel.deslogar()
            resposta = str.encode('+OK 202')
        except LoginRequerido:
            resposta = str.encode('+OK 411')

    elif comando == 'LISTAR' and len(solicitacao) == 1:
        quartos = hotel.listar_quartos()
        resposta = str.encode(f'+OK 207 {quartos}')

    elif comando == 'PROCURAR' and len(solicitacao) == 2:
        numero_quarto = int(solicitacao[1])
        try:
            dados_quarto_procurado = hotel.procurar_quarto_numero(numero_quarto)
            resposta = str.encode(f'+OK 204 {dados_quarto_procurado}' )

        except QuartoInexistenteException:
            resposta = str.encode(f'-ERR 407 ')
        except QuartoIndisponivelException:
            resposta = str.encode(f'-ERR 409 ')

    elif comando == 'PRECO' and len(solicitacao) == 2:
        preco = float(solicitacao[1])
        try:
            quartos = hotel.listar_quartos_preco(preco)
            resposta = str.encode(f'+OK 207 {quartos}')
        except PrecoNegativo:
            resposta = str.encode(f'-ERR 408 ')

    elif comando == 'RESERVAR' and len(solicitacao) == 5:
        numero_quarto = int(solicitacao[1])
        nome_usuario = solicitacao[2]
        data_checkin = solicitacao[3]
        data_checkout = solicitacao[4]

        try:
            hotel.reservar_quarto(numero_quarto, nome_usuario, data_checkin, data_checkout)
            resposta = str.encode('+OK 203')
        except UsuarioInexistenteException:
            resposta = str.encode('-ERR 403')
        except QuartoInexistenteException:
            resposta = str.encode('-ERR 407')
        except QuartoIndisponivelException:
            resposta = str.encode('-ERR 409')
        except DataInvalidaException:
            resposta = str.encode('-ERR 410')
        except FormatoDataInvalidoException:
            resposta = str.encode('-ERR 411')
        except LimiteDiariasException:
            resposta = str.encode('-ERR 412')
        except LimiteDataFuturaException:
            resposta = str.encode('-ERR 413')

    else:
        resposta = str.encode('-ERR 400')

    socket_cliente.send(resposta)
    return True

def processar_clientes(socket_cliente, endereco_cliente):
    '''
    Função responsável por processar conexões de clientes.
    '''
    print(f'Novo cliente conectado: {endereco_cliente}')

    while True:
        solicitacao = socket_cliente.recv(TAM_MSG)

        # Se não tiver solicitação ou se não entra nas solicitações desejadas, ele sai.
        if not solicitacao or not atender_cliente(socket_cliente, endereco_cliente, solicitacao):
            break

    print('Desconectando do cliente', endereco_cliente)
    socket_cliente.close()

hotel = Hotel()

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind((HOST, PORT))
socket_servidor.listen(50)

print('=' * 53)
print('🏨 Servidor de H-RES iniciado. Aguardando conexões...')
print('=' * 53, end='\n\n')

while True:
    try:
        # Aguardando conexões de clientes
        socket_cliente, endereco_cliente = socket_servidor.accept()
    except: break

    threading.Thread(target=processar_clientes, args=(socket_cliente, endereco_cliente)).start()

socket_servidor.close()
