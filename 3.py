def tabuada(numero):
    contador = 1
    
    while contador <= 10:
        print(f"{numero} x {contador} = {numero * contador}")
        contador += 1

numeros = [2, 5, 7]

for n in numeros:
    print(f"\nTabuada do {n}:")
    tabuada(n)