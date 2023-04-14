# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Digite uma nota entre zero e dez: "))

while not nota < 0 and not nota > 11:
    int(input("Digite uma nota entre zero e dez: "))