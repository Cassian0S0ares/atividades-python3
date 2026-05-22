def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

alunos = [
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "Carlos", "notas": [5, 6, 5]},
    {"nome": "Mariana", "notas": [4, 3, 5]},
    {"nome": "João", "notas": [10, 9, 8]}
]

print("RELATÓRIO DOS ALUNOS\n")

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    situacao = situacao_aluno(media)

    print(f"Nome: {aluno['nome']}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 25)