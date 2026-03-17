n = int(input("Quantidade de alunos: "))
soma = 0

for i in range(n):
    nota = float(input(f"Nota do aluno {i+1}: "))
    if nota >= 5.0:
        soma += nota

print("Soma das notas >= 5:", soma)