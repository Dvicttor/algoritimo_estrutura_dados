# 9. Menu de opções
op = int(input("1-Somar, 2-Subtrair, 3-Multiplicar, 4-Dividir: "))
a, b = map(int, input("Digite dois números: ").split())
if op == 1:
    print(a + b)
elif op == 2:
    print(a - b)
elif op == 3:
    print(a * b)
elif op == 4:
    print(a / b)
else:
    print("Opção inválida")


