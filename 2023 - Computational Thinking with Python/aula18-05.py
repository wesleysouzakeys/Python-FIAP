# Função que obriga o usuário a digitar um número e tem até x tentativas
def input_numerico(msg, tentativas):
    num = input(msg)
    i=1

    while not num.isnumeric() and i < tentativas:
        print("Tem que ser numero!")
        num = input(msg)
        i+=1

    if num.isnumeric():
        num = int(num)
        return num
    else:
        print("Erro")
        return False

def retorna_opcao(opcoes, msg):
    opcao = input(msg)
    while opcao not in opcoes:
        print("Digite uma opção válida!")
        opcao = input(msg)
    return opcao

def local_maior(lista):
    maior = lista[0]
    indice_maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

def minha_soma(lista):
    soma = 0
    for num in lista:
        soma+=num
    return soma

def media(lista):
    soma = minha_soma(lista)
    return soma/len(lista)

lista = [21, 23, 534, 5, 778, 43, 54, 4]
carros = ["up", "fusca", "uno", "kombi", "celtinha", "ka", "gol", "corsa"]

indice_maior = local_maior(lista)
print(f"O maior elemento é {lista[indice_maior]} no indice {indice_maior}")
print(f"O carro mais caro é {carros[indice_maior]}")

vinhos = ["tinto", "suave", "rose"]
vinho = input("Diga o vinho: ")
while vinho not in vinhos:
    vinho = input("Diga o vinho: ")

opcoes = ["sim", "nao"]
opcao = input("Diga sim ou nao: ")
while opcao not in opcoes:
    opcao = input("Diga sim ou nao: ")