numero1 = float(input("digite primeiro numero:"))
numero2 = float(input("digite o segundo numero:"))


if numero1 >= numero2:
    total =  float(numero1 /numero2)
    print("O número 1 é o maior número. O resultado é: ", total)

else:
    total = float(numero2 / numero1)
    print("O número 2 é o maior número. O resultado é: ", total)
