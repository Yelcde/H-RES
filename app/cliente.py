import socket
import sys

from processa_solicitacao import processa_solicitacao

HOST = 'localhost'
PORTA = 50000

# Obter parâmetros de conexão (HOST e PORTA) pelo terminal caso seja informado
if len(sys.argv) == 2:
    HOST = sys.argv[1]
elif len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORTA = int(sys.argv[2])


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
