# c = lista[0]
# lista[0] = lista[len(lista) - 1]
# lista[len(lista) - 1] = c
# print(lista)

# c = lista[1]
# lista[1] = lista[len(lista)-1-1]
# lista[len(lista)-1-1] = c
# print(lista)

# lista = ["dan", "allen", "maicon", "boanerges", "joao", "marquin", "celiton"]

# for i in range(len(lista)//2):
#     # Salva o primeiro item da lista em uma variável temporária
#     temp = lista[i]
#     # Atribui para o primeiro valor da lista o último valor da lista
#     lista[i] = lista[len(lista) - 1 - i]
#     # Atribui ao ultimo valor da lista o valor guardado na variável temporária.
#     lista[len(lista) - 1 - i] = temp
#     print(lista)

# --------------------------------------------------------------------------------------------

# carros = ["fusca", "corsa", "golf", "celtinha", "saveiro", "uno"]
# precos = [100, 120, 150, 1000000, 200, 50000]
# maior = precos[0]
# indice_maior = 0
# for i in range(len(precos)):
#     if precos[i]>maior:
#         maior = precos[i]
#         indice_maior = i
#         print(f"o maior é {maior} no indice {indice_maior}")

# print(f"O carro mais caro é o {carros[indice_maior]}")    

# --------------------------------------------------------------------------------------------

# def checa_numero(num):
#     while not num.isnumeric():
#         num = input("Diga um número!!!: ")
#     num = int(num)
#     return num

# a = input("Diga um número: ")
# a = checa_numero(a)
# print(a)
# b = input("Quantos vinhos você quer? ")
# b = checa_numero(b)

# Função que recebe um número e verifica se é par ou não

# def isPar(num):
#     num = int(num)
#     num % 2 == 0
#     if (num % 2 == 0) == True:
#         return print(f"{num} é par")
#     else:
#         return print(f"{num} é impar")

# num = input("Digite um número: ")

# isPar(num)

