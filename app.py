# 1 - Verificar se um número é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 2 - Classificar idade em categorias
idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Você é uma criança.")
elif 13 <= idade <= 18:
    print("Você é um adolescente.")
elif idade > 18:
    print("Você é um adulto.")
else:
    print("Idade inválida.")

# 3 - Verificar nome de usuário e senha
usuario_correto = "usuario123"
senha_correta = "senha123"
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")

# 4 - Determinar o quadrante de um ponto no plano cartesiano
x = float(input("Digite a coordenada x do ponto: "))
y = float(input("Digite a coordenada y do ponto: "))

if x > 0 and y > 0:
    print("O ponto está no Primeiro Quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no Segundo Quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no Terceiro Quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no Quarto Quadrante.")
else:
    print("O ponto está no eixo ou na origem.")