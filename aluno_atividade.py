# Cadastro simples de aluno

nome = input("Digite o nome do aluno: ")
cpf = input("Digite o CPF do aluno: ")
data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")

print("\n--- Dados do Aluno ---")
print("Nome:", nome)
print("CPF:", cpf)
print("Data de Nascimento:", data_nascimento)

print("\n--- Nome repetido 10 vezes ---")
for i in range(10):
    print(nome)