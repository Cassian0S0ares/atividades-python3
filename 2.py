def analisa(numero):
    if numero >= 1:
        return 'Positivo'
    elif numero == 0:
        return 'Zero'
    else:
        return 'Negativo'
lista = [4,-5,0,10,-8,4]
for numero in lista:
    print(analisa(numero))