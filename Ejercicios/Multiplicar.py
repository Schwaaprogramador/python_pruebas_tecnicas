

# Haz una funcion multiplicar sin utlizar el simbolo de la multiplicacion #


def multiplicar(a , b):
    total = 0
    for num in range(b):
        total += a
        
    return total



numero = multiplicar(4, 5 )
print(numero)