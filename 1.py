def classifica(i):
    if i >= 8:
        return "Excelente"
    elif i >= 6 and i <= 7:
        return "Aprovado"
    elif i >= 4 and i <= 5:
        return "Recuperação"
    else:
        return "Reprovado"


nota = [10,5,7,3,7,1,8,4,2,5,6]


for i in nota:
    print(classifica(i))
