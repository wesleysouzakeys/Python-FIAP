# Calcule o salário de um programador, cujo salário é função das horas de trabalho semanais. Deverá ser multiplicado o número de horas trabalhadas por 4,5 semanas. O resultado encontrado é o total de horas-mês dedicado. Deve ser acrescido a esse valor 10%, devido à gratificação por desempenho. Para calcular, multiplique o salário-base por esse percentual. Além disso, existe o DSR - Descanso Semanal Remunerado que corresponde a 1/6 sobre a remuneração total, portanto deve ser calculado sobre a soma anteriormente verificada.

import os

def forca_numero(valor):
    if (not valor.isnumeric()):
        while not valor.isnumeric():
            valor = input("Valor inválido, digite apenas valores numéricos: ")
        return int(valor)
    return int(valor)
      
horas_trabalhadas = forca_numero(input("Digite as suas horas trabalhadas: "))
salario_hora = forca_numero(input("Digite o valor do seu salário/hora: "))
salario_total = horas_trabalhadas * salario_hora

# Limpa terminal
os.system('cls')

print(f"Seu salário com base nas horas-mês é de {salario_total}")

salario_total += salario_total * 0.10
print(f"Adicionado a gratificação de 10%, seu novo saldo é de {salario_total}")

salario_total += salario_total / 6
print(f"Adicionado o DSR, seu novo saldo é de {salario_total:.2f}")