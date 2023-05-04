# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite uma nota entre zero e dez: "))

while not (nota > 0 and nota < 11):
    nota = int(input("A nota inserida não atende os requisitos, Digite uma nota entre zero e dez: "))

# 2 - Faça um programa que leia e valide as seguintes informações: 
# - a. Nome: maior que 3 caracteres; 
# - b. Idade: entre 0 e 100. 
# - c. Salário: maior que zero. 
# - d. Sexo: 'f' ou 'm'. 
# - e. Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
while len(nome) < 4:
    nome = input("Seu nome precisa conter mais que 3 caracteres, Digite novamente: ")

idade = int(input("Digite sua idade: "))
while not (idade > 0 and idade < 101):
    idade = int(input("Sua idade precisa ser entre 0 e 100, Digite novamente: "))

salario = int(input("Digite seu salário: "))
while not salario > 0:
    salario = int(input("O valor inserido não é um número ou não é maior que zero, Digite novamente: "))

sexo = input("Digite seu sexo - (f / m): ")
while not (sexo == "f" or sexo == "m"):
    sexo = input("Valor não reconhecido, Digite novamente (f / m): ")

estadoCivil = input("Digite seu estado Civil (s / c / v / d): ")
while not (estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d"):
    estadoCivil = input("Valor não recinhecido, Digite novamente (s / c / v / d): ")

# 3 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

t = 0
a = 80000
b = 200000

while a <= b:
    a*=1.03
    b*=1.015
    t+=1
print(t) 

# 4 - Faça um programa que leia 5 números e informe a soma e a média dos números.

acc = 1
soma = 0 
media = 0

while acc < 6: 
    num = int(input(f"Digite o {acc}º número: "))
    soma+= num
    acc+=1

media = soma / 5

print(f"A soma de seus números é {soma}, e a média é {media}")

# 5 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite o segundo número: "))

while num1 < num2 - 1:
    num1+=1
    print(num1)

# 6 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("Digite seu nome de Usuário: ")
pwd = input("Digite sua senha: ")

while user == pwd:
    print("Seu nome de Usuário não pode ser igual à sua senha, tente novamente")
    user = input("Digite seu nome de Usuário: ")
    pwd = input("Digite seu nome de Usuário: ")

    user.lower()
    pwd.lower()

# 7 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: 
# Tabuada de 5: 
# 5 X 1 = 5 
# 5 X 2 = 10 
# ... 
# 5 X 10 = 50

# acc = 1
# acc2 = 1

while acc2 < 11:
    while acc < 11:
        print(f"{acc} x {acc2} = {acc * acc2}")
        # print(acc)
        acc += 1
    print("")
    acc = 1
    acc2 +=1

# GPT's Version
# acc = 1
# while acc <= 10:
#     acc2 = 1
#     while acc2 <= 10:
#         print(f"{acc} x {acc2} = {acc * acc2}")
#         acc2 += 1
#     print("")
#     acc += 1