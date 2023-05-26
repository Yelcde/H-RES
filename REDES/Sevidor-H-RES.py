import socket

# Configurações do servidor
endereco_servidor = 'localhost'
porta_servidor = 50000

# Criação do socket TCP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket ao endereço e porta do servidor
socket_servidor.bind((endereco_servidor, porta_servidor))


socket_servidor.listen()

print('Servidor de hotel iniciado. Aguardando conexões...')

while True:
    # Aguarda uma conexão do cliente
    socket_cliente, endereco_cliente = socket_servidor.accept()
    print('Cliente conectado:', endereco_cliente)

    # Solicitações do cliente
    while True:
        # Recebe a solicitação do cliente
        solicitacao = socket_cliente.recv(1024).decode()

        if not solicitacao:
            # Se a solicitação estiver vazia, a conexão foi encerrada pelo cliente
            print('Conexão encerrada pelo cliente:', endereco_cliente)
            break

        # Lógica para processar a solicitação do cliente
        if solicitacao == 'disponibilidade':
            # Consulta a disponibilidade de quartos no banco de dados
            disponibilidade = consultar_disponibilidade()
            resposta = f'Disponibilidade: {disponibilidade}'
        elif solicitacao == 'reserva':
            # Processa a reserva do quarto no banco de dados
            resultado = processar_reserva()
            resposta = 'Reserva efetuada com sucesso!' if resultado else 'Falha na reserva.'
        elif solicitacao == 'cancelar':
            # Cancela a reserva no banco de dados
            resultado = cancelar_reserva()
            resposta = 'Reserva cancelada com sucesso!' if resultado else 'Falha ao cancelar reserva.'
        else:
            resposta = 'Solicitação inválida.'

        # Envia a resposta para o cliente
        socket_cliente.send(resposta.encode())

    # Encerra a conexão com o cliente
    socket_cliente.close()

# Encerra o socket do servidor
socket_servidor.close()
