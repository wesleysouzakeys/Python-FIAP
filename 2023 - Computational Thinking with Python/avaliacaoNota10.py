# Código da terceira avaliação de Python do 1° Semestre de Engenharia de Software da FIAP, 
# da qual tirei nota máxima (10).

def input_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input("Por favor digite um número válido: ")
    
    num = int(num)
    return num

def verifica_opcoes(frase, opcoes):
    opcao = input(frase)

    while opcao not in opcoes:
        opcao = input(f"Digite uma das opções existentes: {opcoes}")
    
    return opcao

def acha_maior(lista):
    maior = lista[0]
    indice_maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    
    return indice_maior

def acha_menor(lista):
    menor = lista[0]
    indice_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    
    return indice_menor

def soma(lista):
    soma = 0
    for elem in lista:
        soma+=elem

    return soma

def media(lista):
    total = soma(lista)
    
    return total/len(lista)

precos = [239, 329, 79, 190]
vinhos = ["rose", "tinto", "suave", "bordo"]
escolha = ["continuar", "encerrar"]
total = 0
qtdRose = 0
qtdTinto = 0
qtdSuave = 0
qtdBordo = 0

endereco = input("Seja bem-vindo, digite seu endereço: ")
anoNasc = input_numero("Agora digite seu ano de nascimento: ")


if (2023 - anoNasc) < 18:
    print("Não é permitido a venda de bebidas alcoolicas para menores de idade")
else:
    print(f"O custo médio de um vinho é R${media(precos)}, o vinho mais caro é o {vinhos[acha_maior(precos)]}, custando {precos[acha_maior(precos)]}, e o mais barato é o {vinhos[acha_menor(precos)]}, custando {precos[acha_menor(precos)]}")

    while True:
        vinho = verifica_opcoes("Qual vinho você deseja comprar? (rose/tinto/suave/bordo): ", vinhos)
        qtd = input_numero("Quantos vinhos deseja comprar: ")

        if vinho == "rose":
            qtdRose += qtd
            total += qtd * 239
        elif vinho == "tinto":
            qtdTinto += qtd
            total += qtd * 329
        elif vinho == "suave":
            qtdSuave += qtd
            total += qtd * 79
        else:
            qtdBordo += qtd
            total += qtd * 190

        destino = verifica_opcoes("Você deseja continuar ou encerrar a sua compra ? (continuar/encerrar): ", escolha)

        if destino == "continuar":
            continue;
        else:
            break;

if total > 500:
    print(f"Muito obrigado, o valor total de sua compra foi de R${total} e receberá frete grátis! Você comprou {qtdRose} vinho(s) rose, {qtdTinto} vinho(s) tintos, {qtdSuave} vinho(s) suave e {qtdBordo} vinho(s) bordo, sua compra será entregue em {endereco}")
else:
    print(f"Muito obrigado, o sub-total de sua compra foi de R${total} e você pagará R$20,00 de frete, portanto o total é de {total + 20}! Você comprou {qtdRose} vinhos rose, {qtdTinto} vinhos tintos, {qtdSuave} vinhos suave e {qtdBordo} vinhos bordo, sua compra será entregue em {endereco}")

vinhos = ["rose", "tinto", "suave", "bordo"]