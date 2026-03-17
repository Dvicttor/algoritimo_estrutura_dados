n = int(input("Quantidade de alunos: "))
soma = 0
contador = 0

for i in range(n):
    idade = int(input(f"Idade do aluno {i+1}: "))
    if 25 < idade < 40:
        soma += idade
        contador += 1

if contador > 0:
    media = soma / contador
    print("Média:", media)
else:
    print("Nenhum aluno na faixa etária.")