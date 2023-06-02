# Importações
import threading
import socket
from entidades.Hotel import Hotel

# Configurações do servidor
TAM_MSG = 1024
HOST = 'localhost'
PORT = 50000

hotel = Hotel()

#Função para processar as solicitações dos clientes
def atender_clientes(socket_cliente, endereco_cliente, solicitacao):
    # Recebe a solicitação do cliente e decodifica
    solicitacao = solicitacao.recv(TAM_MSG).decode()
        #Avisando que o cliente mandou mensagem
    print(f'Cliente mandou: {solicitacao}')

        # processar a solicitação do cliente separando a tupla e tirando aquela parte desnecessária.
    solicitacao = solicitacao.split()
    comando = solicitacao[0].upper()
    resposta = ''

    # solicitação de registro que vai ter registrar no [0], a senha e o usuário
    if comando == 'REGISTRAR' and len(solicitacao) == 3:
        usuario = solicitacao[1]
        senha = solicitacao[2]

        # registro do usuário
        # essa função precisa existir na classe hotel.
        resposta = ''
        registrou = hotel.registrar_cliente(usuario, senha)

        if registrou:
            resposta = (str.encode('+OK 200 Usuário registrado com sucesso.'))
        else:
            # Erros no registro do usuário
            resposta = (str.encode(f'-ERR 403 Usuário já existe.'))

    # solicitação de login para pegar somente o comando [0] que vai ter o login, senha e usuário
    elif comando == 'LOGIN' and len(solicitacao) == 3:
        usuario = solicitacao[1]
        senha = solicitacao[2]

        resposta = ''
        logou = hotel.login_cliente(usuario, senha)

        if logou:
            # login do usuário com sucesso
            resposta = (str.encode('+OK 201 Usuário logado com sucesso.'))
        else:
            # Erros no login
            resposta = (str.encode('-ERR 403 Usuário não existe.'))

    elif comando == 'RESERVAR':
        # reservar quarto do usuário
        if hotel.login_usuario(usuario, senha):
            resposta = (str.encode('+OK 201 Usuário logado com sucesso. \n'))

    elif comando == 'SAIR':
        try:
            socket_cliente.send(str.encode('+OK\n'))
            return False

        except:
            socket_cliente.send(str.encode('-ERR Comando inválido\n'))
            return True

    # Comando errado geral
    else:
        solicitacao = ' '.join(solicitacao[:-1])
        resposta = (str.encode(f'-ERR 400 Comando inválido.'))

    socket_cliente.send(resposta)


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

# Encerra o socket do servidor
socket_servidor.close()
