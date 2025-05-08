notas = []
while True:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)

aprovados = sum(1 for nota in notas if nota >= 5)
reprovados = sum(1 for nota in notas if nota < 5)
total_alunos = len(notas)

print("\nResultados:")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")
print(f"Quantidade de alunos que fizeram a prova: {total_alunos}")