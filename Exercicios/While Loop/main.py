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

# 3- Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

t = 0
a = 80000
b = 200000

while a <= b:
    a*=1.03
    b*=1.015
    t+=1
print(t) 