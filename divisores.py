# Exercício de verificar divisores de um dado número com duas opções de exibição.

contagem = 1
divisores = []

def forca_escolha(texto, opcoes):
    opcao = input(texto)
    if opcao in opcoes:
            return opcao
    else:
        while not (opcao in opcoes):
            opcao = input("O valor digitado não é válido, tente novamente: ")
    return opcao

def forca_digitar_numero():
    valor = input("Digite o número a ser descoberto os divisores: ")

    if valor.isnumeric():
            return int(valor)
    else:
        while not valor.isnumeric():
            valor = input("O valor digitado não é um número, tente novamente: ")
            if valor.isnumeric():
                return int(valor)
     
numero_desejado = forca_digitar_numero()

escolha = forca_escolha("Para ver todos os passos digite 1 | Para ver apenas os divisores digite 2: ", ["1", "2"])

if escolha == "1":
    while (contagem <= numero_desejado):
        if (numero_desejado % contagem == 0):
            print(f"{numero_desejado} é divisível por {contagem}")
        else:
            print(f"{numero_desejado} não é divisível por {contagem}")
        contagem+=1
else:
    while (contagem <= numero_desejado):
        if (numero_desejado % contagem == 0):
            divisores.append(contagem)
        contagem+=1
    print(divisores)
