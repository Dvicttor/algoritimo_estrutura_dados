n = int(input("Quantidade de alunos: "))
soma = 0
contador = 0

for i in range(n):
    nota = float(input(f"Nota do aluno {i+1}: "))
    if 5.0 < nota < 7.0:
        soma += nota
        contador += 1

if contador > 0:
    media = soma / contador
    print("Média:", media)
else:
    print("Nenhuma nota no intervalo.")