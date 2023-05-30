#!/usr/bin/env python3
# Importações
from threading import *
import socket
# import hotel


# Configurações do servidor
HOST = 'localhost'
PORT = 50000

# Os semáforos
lock_registro_semáforo = Lock()

#Função para processar as solicitações dos clientes
def atender_clientes(socket_cliente, endereco_cliente, solicitacao):
    # Recebe a solicitação do cliente e decodifica
    solicitacao = solicitacao.recv(1024).decode().strip()
    #Avisando que o cliente mandou mensagem
    print(f'Cliente mandou: {solicitacao}')

    # processar a solicitação do cliente separando a tupla e tirando aquela parte desnecessária.
    solicitacao_partida = solicitacao.split()

    # solicitação de registro    
    if solicitacao_partida[0].upper() == 'REGISTRAR':
        usuario = solicitacao_partida[1]
        senha = solicitacao_partida[2]
        
    # Bloqueia o acesso ao elemento txt de registro que vai ser escrito agora
        lock_registro_semáforo.acquire()

        # registro do usuário
        # essa função precisa existir na classe hotel
        if registro_usuario (usuario, senha):
            return ('+OK 20 frase que lucas colocou')
        else:
            return ('-ERR 43 Registration failed')

        # Libera o acesso ao recurso compartilhado
        register_lock.release()

    else:
        response = "-ERR 40 regristo inválido"    
                
                
                # Consulta a disponibilidade de quartos no banco de dados
                
                disponibilidade = consultar_disponibilidade()
                resposta = f'Disponibilidade: {disponibilidade}'
            elif solicitacao == 'reserva':
                try:
                # Processa a reserva do quarto no banco de dados
                    resultado = processar_reserva()
                    resposta = 'Reserva efetuada com sucesso!' 
                except:
                    resultado else 'Falha na reserva.'
            elif solicitacao == 'cancelar':
                # Cancela a reserva no banco de dados
                resultado = cancelar_reserva()
                resposta = 'Reserva cancelada com sucesso!' if resultado else 'Falha ao cancelar reserva.'
            else:
                resposta = 'Solicitação inválida.'

            socket_cliente.send(resposta.encode())
            if not solicitacao:
            # Se a solicitação estiver vazia, a conexão foi encerrada pelo cliente
                print('Conexão encerrada pelo cliente:', endereco_cliente)
                break



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