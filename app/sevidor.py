import socket
import threading

from entidades.Hotel import Hotel
from entidades.Quarto import Quarto
from excecoes import UsuarioInexistenteException, SenhaIncorretaException, QuartoIndisponivel, LoginRequerido

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
    # Recebe a solicitação do cliente e decodifica
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

    elif comando == 'LISTAR' and len(solicitacao) == 2:
        listar = hotel.listar_quartos_disponiveis()
        resposta = str.encode(f'+OK 207 {listar}')

    elif solicitacao[2].upper() == 'NUMERO' and len(solicitacao) == 5:
        pass

    elif solicitacao[2].upper() == 'PREÇO' and len(solicitacao) == 5:
        pass

    elif comando == 'RESERVAR' and len(solicitacao) == 2:
        usuario = solicitacao[1]

        try:
            # Se o usuário tiver logado = ok
            logado = hotel.login_usuario(usuario, senha)
            # se tiver continua aqui
            if logado:
                # Se a reserva acontecer
                hotel.reservar(usuario, quarto, chekin, checkout)
                resposta = str.encode('+OK 203')
                # se o quarto estiver indisponível e a reserva não acontecer
        except QuartoIndisponivel:
            resposta = str.encode('+OK 405')
        except LoginRequerido: # se usuário não tiver logado
            resposta = str.encode('-ERR 401')

    elif comando == 'SAIR':
        return False

    # Comando errado geral inválido
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
