def imprimirNumeros():
    for i in range(1, 100):
        print("El numero actual es...")
        print(i)

imprimirNumeros()

# - - - - - - - - - - - - - - - - - - - - - - - 

def imprimirNumeros_bis(limite):
    for i in range(1, limite):
        print("El numero actual es...")
        print(i)


imprimirNumeros_bis(100)

# - - - - - - - - - - - - - - - - - - - - - - - 

def imprimirNumerosPares(limite):
    for i in range(1, limite):

        if i % 2 == 0:
            print("El numero es par y es el siguiente...")
            print(i)


imprimirNumerosPares(100)
