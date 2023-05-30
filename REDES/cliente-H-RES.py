#!/usr/bin/env python3
import socket

# Configurações do servidor
endereco_servidor = 'localhost'
porta_servidor = 12345

# Criação do socket TCP
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
socket_cliente.connect((endereco_servidor, porta_servidor))

# Função para enviar uma solicitação e receber a resposta do servidor
def enviar_solicitacao(solicitacao):
    socket_cliente.send(solicitacao.encode())
    resposta = socket_cliente.recv(1024).decode()
    return resposta


resposta = enviar_solicitacao('disponibilidade')
print('Resposta do servidor:', resposta)

resposta = enviar_solicitacao('reserva')
print('Resposta do servidor:', resposta)

resposta = enviar_solicitacao('cancelar')
print('Resposta do servidor:', resposta)

# Encerra a conexão com o servidor
socket_cliente.close()