n = int(input("Quantidade de alunos: "))
soma = 0

for i in range(n):
    nota = float(input(f"Nota do aluno {i+1}: "))
    soma += nota

print("Soma das notas:", soma)