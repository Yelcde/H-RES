#!/usr/bin/env python3
# Importações
import threading
import socket
from threading import Lock
import sys
# import hotel


# Configurações do servidor
TAM_MSG = 1024
HOST = 'localhost'
PORT = 50000

# Os semáforos
lock = Lock()

#Função para processar as solicitações dos clientes
def atender_clientes(socket_cliente, endereco_cliente, solicitacao):
    # Recebe a solicitação do cliente e decodifica
    solicitacao = solicitacao.recv(TAM_MSG).decode().strip()
        #Avisando que o cliente mandou mensagem
    print(f'Cliente mandou: {solicitacao}')

        # processar a solicitação do cliente separando a tupla e tirando aquela parte desnecessária.
    solicitacao = solicitacao.split()
    
    # Bloqueia o acesso ao elemento txt de registro que vai ser escrito agora
    with lock:
        # solicitação de registro    
        if solicitacao[0].upper() == 'REGISTRAR' and len(solicitacao) == 2:
            usuario = solicitacao_partida[1]
            senha = solicitacao_partida[2]

            # registro do usuário
            # essa função precisa existir na classe hotel. JOHNNER CRIE O HOTEL!
            if hotel.registro_usuario(usuario, senha):
                resposta = (str.encode('+OK 200 Usuário registrado com sucesso. \n'))
                socket_cliente.send(resposta)
            else:
                resposta_erro = (str.encode(f'-ERR 403 Usuário já existe. \n'))
                socket_cliente.send(resposta_erro)

        else:
            resposta_erro = (str.encode(f'-ERR 430 Comando inválido. \n'))
            socket_cliente.send(resposta_erro)
             # libera o acesso ao recurso compartilhado

        with lock:
        # solicitação de login 
            elif solicitacao[0].upper() == 'LOGIN' and len(solicitacao) == 3:

                # login do usuário
                if hotel.login_usuario(usuario, senha):
                        resposta = (str.encode('+OK 201 Usuário logado com sucesso. \n'))
                        socket_cliente.send(resposta)
                else:
                    resposta = (str.encode('-ERR 403 Usuário não existe. \n'))
                    socket_cliente.send(resposta)
            else:

            elif solicitacao[0].upper() == 'RESERVAR':

                # reservar quarto do usuário
                if hotel.login_usuario(usuario, senha):
                        resposta = (str.encode('+OK 201 Usuário logado com sucesso. \n'))
                        socket_cliente.send(resposta)
                else:
                    resposta = (str.encode('-ERR 403 Usuário não existe. \n'))
                    socket_cliente.send(resposta)
            else:


# Função para processar TODOS os clientes que vão se conectar, atender mais de um
def processar_clientes(socket_cliente, endereco_cliente, solicitacao):
    # conecta com um novo cliente
    print('Conectado com', endereco_cliente)
    
    while True:
        # decodifica a solicitação nova enviada
        solicitacao = socket_cliente.recv(1024)
        # Se não tiver solicitação ou se não entra nas solicitações desejadas, ele sai.
        if not solicitacao or not atender_clientes(socket_cliente, endereco_cliente, solicitacao):break
        
    print('Desconectando do cliente', endereco_cliente)
    socket_cliente.close()

# Criação do socket TCP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e porta do servidor
socket_servidor.bind((HOST, PORT))

# servidor escutando na porta
socket_servidor.listen(50)

print('Servidor de hotel iniciado. Aguardando conexões...')

while True:
    try:
    # Aguarda uma conexão do cliente
        socket_cliente, endereco_cliente = socket_servidor.accept()
        # Cliente aceita a conexão com o servidor
        print('Cliente conectado:', endereco_cliente)

    # Se não houver conexão, o servidor sai.
    except: break
    # Cria uma Thread diferente para cada cliente
    threading.Thread(target=processar_clientes, args=(socket_cliente, endereco_cliente)).start()
# Encerra a conexão com o cliente
socket_cliente.close()

# Encerra o socket do servidor
socket_servidor.close()