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
    except:
        solicitacao = 'SAIR'
        print('Desconectado...')
        break
    if solicitacao == '':
        print('Comando indefinido.)

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
        mensagem_decode = dados.decode().split('\n') #Decodifica e joga numa lista separando por "/n", pegando só o indice 0 
        # Salva a mensagem decodificada e partida numa nova variavel
        dados = mensagem_decode 
        print(dados)
        
        if dados[1] == '200':
            LOGIN = True
            
        elif dados[1] == '':
            num_arquivos = int(msg_status.split()[1]) #Pegar o indice [1], pq é depois do +OK pq é 
                                                      # a quantidade de arquivos que tem para transformar em inteiro
            dados = dados.decode()# transformar em string
            while True:
                arquivos = dados.split('\n')
                residual = arquivos[-1]
                # último sem \n fica para próxima
                for arq in arquivos[:-1]:
                    print(arq)
                    num_arquivos -= 1
                if num_arquivos == 0: break
                dados = sock.recv(TAM_MSG)
                if not dados: break
                dados = residual + dados.decode()

        elif cmd[0] == 'GET':
            nome_arq = " ".join(cmd[1:])
            print('Recebendo:', nome_arq)
            arq = open(nome_arq, "wb")
            tam_arquivo = int(msg_status.split()[1])
            while True:
                arq.write(dados)
                tam_arquivo -= len(dados)
                if tam_arquivo == 0: break
                dados = sock.recv(TAM_MSG)
                if not dados: break
            arq.close()
sock.close()