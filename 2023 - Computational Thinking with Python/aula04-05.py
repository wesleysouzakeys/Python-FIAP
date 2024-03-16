'''
lista = [i**2 for i in range(15)]

for i in range(len(lista))
    print(lista[i])
    
profs = ["Wesley", "Kayque", "Laís", "Guilherme", "Samuel"]
for elem in profs:
    print(elem)
for i in range(len(profs)):
    print(profs[i])
    
profs[0] = "Allen"
print(profs)

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for elem in lista:
    lista = 1
    
print(lista)

for i in range(len(lista)):
    lista = 1
    
print(lista)

lista = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
teste = lista[:]
teste = lista[7:]
teste = lista[:7]
teste = lista[7:13]
'''

#Peguem uma lista qualquer e invertam a ordem de todos os elementos

#lista = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# lista = ["Kayque", "Laís", "Guilherme", "Samuel"]

# # Algoritmo para inverter listas
# for i in range(len(lista)//2):
#     temp = lista[i]
#     lista[i] = lista[len(lista)-i-1]
#     lista[len(lista) - i - 1] = temp
# print(lista)

# print(lista[::-1])

# listaVazia = []

# while True:
#     elem = input("Digite algo: ")
#     if elem == "sair":
#         break;
#     else:
#         listaVazia.append(elem)
#     print(listaVazia)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaPares = []
listaImpares = []

for elem in lista:
    if elem % 2 == 0:
        listaPares.append(elem)
    else:
        listaImpares.append(elem)

print(listaPares)
print(listaImpares)