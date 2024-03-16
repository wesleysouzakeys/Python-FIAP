# i = 0
# acc = 0

# while i < 100:
#     if i % 2 == 0:
#         acc+=1
#     i+=1
    
# -----------------------------------------------------------------------------------

# print(acc)

# i= 0 
# qtd_pares = 0
# while i<10:
#     num - int(input("Diga um numero: "))
#     if num%2==0:
#         qtd_pares+=1
#     i+=1
# print(f"Há {qtd_pares} pares entre 0 e 100") 

# -----------------------------------------------------------------------------------

# cdt = ""
# times = 0

# while cdt == "":
#     letter = input("Digite uma letra: ")
#     if letter == "sair":
#         cdt = letter
#     elif letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         print("É vogal")
#     else:
#         print("Não é vogal")
#     times+=1

# -----------------------------------------------------------------------------------

import os
clear = lambda: os.system('cls')

user = "Wesley"
pwd = "1234"
userInput = ""
pwdInput = ""
cont = 0

while (userInput != user or pwdInput != pwd) and cont < 3:
    userInput = input("Digite seu Usuário: ")
    pwdInput = input("Digite sua Senha: ")

    if userInput == user and pwd == pwdInput:
        print("Acesso Liberado")
    else:
        clear()
        print("Tente novamente")
    
    cont+=1
