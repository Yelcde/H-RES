#!/usr/bin/env python3
import socket
import sys

TAM_MSG = 1024         # Tamanho do bloco de mensagem
HOST = 'localhost'    # IP do Servidor
PORT = 50000           # Porta que o Servidor escuta
LOGIN = False

sys.path.append('.')

from estruturas.avl import AVLTree

avl = AVLTree()


# Pegar o IP e a porta que o cliente vai acessar e se conectar
if len(sys.argv) == 2:
    HOST = sys.argv[1]
elif len(sys.argv) == 3:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

print('H-RES Sistema', HOST+':'+str(PORT)+'\n')

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
print('Para encerrar use SAIR, CTRL+D ou CTRL+C\n')

while True:
    #Transformando a mensagem de acordo com a função decode_cmd_usr
    try:
        solicitacao = input() # pegar a mesasagem
        # REGISTRAR lucas senha123
    except:
        solicitacao = 'SAIR'
        print('Desconectado...')
        break
    if solicitacao == '':
        print('Comando indefinido.')

    # Se não estiver logado, direciona para o registro
    if LOGIN == False:
        if solicitacao.split()[0].upper() == 'REGISTRAR' or solicitacao.split()[0].upper() == 'LOGIN':


            # envia a mensagem codificada
            sock.send(str.encode(solicitacao))
            # Recebe uma resposta e salva na variavel dados
            dados = sock.recv(TAM_MSG) 
            # Se não receber NADA DO SERVIDOR, encerra 
            if not dados: break

            # Mensagem enviada pelo sevidor é decodificadaa
            mensagem_decode = dados.decode().split()
            # Salva a mensagem decodificada e partida numa nova variavel
            dados = mensagem_decode 
            print(dados)
            
            if dados[1] == '200':
                LOGIN = True
sock.close()