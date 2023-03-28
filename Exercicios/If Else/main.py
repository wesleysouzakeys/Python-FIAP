import datetime

#1 Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.

num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))

if num1 > num2:
    print(f"O primeiro número: {num1}, é maior que o segundo número: {num2}")
else:
    print(f"O segundo número: {num2}, é maior que o primeiro número: {num1}")

#2 Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês que ela nasceu.)

today = datetime.date.today()

year = today.year

birthYear = int(input("Digite o Ano de seu nascimento: "))
 
if year - birthYear < 16:
    print("Você não pode votar ainda!")
else:
    print("Você já pode votar!")

#3 Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
#   ACESSO PERMITIDO caso a senha seja válida.
#   ACESSO NEGADO caso a senha seja inválida.

pwd = input("Digite sua senha: ")

if pwd == "1234":
    print("Acesso Permitido!")
else: 
    print("Acesso Negado!")

#4 As maçãs custam R$ 0,30 cada uma se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.

qtd = int(input("Quantas maçãs você deseja comprar?: "))

if qtd < 12:
    print(f"Você comprou {qtd} maçãs e o preço foi de R${qtd * 0.25}")
else:
    print(f"Você comprou {qtd} maçãs e o preço foi de R${qtd * 0.30}")

#5 Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3 and num2 > num3:
    print(num3, num2, num1)
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(num2, num3, num1)
elif num2 > num1 and num2 > num3 and num1 > num3:
    print(num3, num1, num2)
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(num1, num3, num2)
elif num3 > num2 and num3 > num1 and num2 > num1:
    print(num1, num2, num3)
else: 
    print(num2, num1, num3)

