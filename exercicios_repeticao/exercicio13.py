num = int(input("Digite um número: "))
primo = True

if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print("É primo")
else:
    print("Não é primo")