print("Olá, seja bem vindo à nossa calculadora de equações de segundo grau!")

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2-4*a*c

x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)
xv=-b/(2*a)
yv=-delta/(4*a)

print(f"x1= {x1} x2= {x2}")

if delta >= 0:
    print(f"x1= {x1}, x2= {x2}")
else:
    print("Não possui raízes reais, ou seja, a parábola não cruza o eixo x")
    print(f"xv= {xv}, yv= {yv}")
