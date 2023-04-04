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

#6 Tendo como entrada a altura e o sexo (codificando da seguinte forma: 1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:
# - Para homens: (72.7 * Altura) - 58
# - Para mulheres: (62.1 * Altura) - 44.7

sexo = int(input("Digite seu Sexo 1-Feminino 2-Masculino: "))
altura = float(input("Digite sua altura: "))

if sexo == 1:
    print(f"Seu peso ideal é: {(62.1 * altura) - 44.7:.2f} kg")
else:
    print(f"Seu peso ideal é: {(72.7 * altura) - 58:.2f} kg")

#7 Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Calcular e imprimir o seguinte:
# - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor da área.
# - Se o número de lados for igual a 4, escrever QUADRADO e o valor da área.
# - Se o número de lados for igual a 5, escrever PENTÁGONO.

sides = int(input("Digite o número de lados do seu polígono: "))

if sides != 3 and sides != 4 and sides != 5:
    print("Seu polígono é desconhecido")
elif sides == 5:
    print("Seu polígono é um pentágono")
else:
    sideSize = float(input("Digite o tamanho em cm de um dos lados: "))
    if sides == 3:
        height = float(input("Digite a altura de seu triângulo: "))
        print(f"Seu polígono é um triângulo e sua área é: {(sideSize * height) / 2} cm")
    elif sides == 4:
        print(f"Seu polígono é um quadrado e sua área é: {sideSize * sideSize} cm")

#8 Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
# - Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO. 
# - Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.

sides = int(input("Digite o número de lados do seu polígono: "))

if sides < 3:
    print("Não é um polígono.")
if sides > 5:
    print("Polígono não identificado.")
elif sides == 5:
    print("Seu polígono é um pentágono")
else:
    sideSize = float(input("Digite o tamanho em cm de um dos lados: "))
    if sides == 3:
        height = float(input("Digite a altura de seu triângulo: "))
        print(f"Seu polígono é um triângulo e sua área é: {(sideSize * height) / 2} cm")
    elif sides == 4:
        print(f"Seu polígono é um quadrado e sua área é: {sideSize * sideSize} cm")

#9 Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
# Considere que o usuário não informará valores iguais.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")

#10 Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, Isóceles ou Escaleno. Sendo que:
# - Triângulo Equilátero: possui os 3 lados iguais.
# - Triângulo Isócele: possui 2 lados iguais.
# - Triângulo Escaleno: possui 3 lados diferentes.

side1 = int(input("Escreva em cm a medida do primeiro lado do seu triângulo: "))
side2 = int(input("Escreva em cm a medida do segundo lado do seu triângulo: "))
side3 = int(input("Escreva em cm a medida do terceiro lado do seu triângulo: "))

if side1 == side2 and side1 == side3:
    print("Seu triângulo é Equilátero pois possui os três lados iguais")
elif (side1 == side2 and side3 != side2) or (side2 == side3 and side1 != side3) or (side3 == side1 and side2 != side1):
    print("Seu triângulo é Isócele pois possui dois lados iguais")
else:
    print("Seu triângulo é Escaleno pois possui três lados diferentes")

# 11 Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
# - Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
# - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
# - Triângulo Acutângulo: possui um três ângulos agudos. (menor que 90º)

# 11 Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
# - Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
# - Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
# - Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)

ang1 = int(input("Escreva quantos graus tem o primeiro ângulo: "))
ang2 = int(input("Escreva quantos graus tem o segundo ângulo: "))
ang3 = int(input("Escreva quantos graus tem o terceiro ângulo: "))

if ang1 + ang2 + ang3 == 180:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        print("Seu triângulo é Retângulo por conter pelo menos um dos ângulos igual a 90 graus")
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        print("Seu triângulo é Obtusângulo por conter pelo menos um dos ângulos maior que 90 graus")
    else:
        print("Seu triângulo é Acutângulo por conter três angulos agudos")
else:
    print("A soma dos seus ângulos não atinge ou ultrapassa 180 graus.")