""" Método que será importado para a classe Hotel e ficará responsável por fazer o login dos usuários """

# Importar o usuário para pegar a senha e o login
from entidades import Usuario

def login_usuario (self, usuario:str, senha:str)-> bool:
    if usuario.senha != senha:
        return False
    
    else:
         return True