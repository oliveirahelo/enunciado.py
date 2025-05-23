
print("faca seu cadrastro ")

nome_de_usuario = input("Digite seu nome: ")
senha_cadastro = input("Crie uma senha: ")

print("faça login") 
nome_login = input("Digite nome seu de usuario: ")
senha_login= input("Digite sua senha: ")


while nome_login != nome_de_usuario or senha_login != senha_cadastro :
    print("nome de usuarios ou senha incorretos")
    nome_login = input("Digite ")
    senha = input("Digite sua senha: ")

print("login bem sucedido!")