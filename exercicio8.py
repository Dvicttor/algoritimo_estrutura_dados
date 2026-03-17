n = int(input("Quantidade de alunos: "))
soma = 0

for i in range(n):
    idade = int(input(f"Idade do aluno {i+1}: "))
    if idade > 25:
        soma += idade

print("Soma das idades maiores que 25:", soma)