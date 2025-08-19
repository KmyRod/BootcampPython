
import numbers

def fib(numero):
    #Precondiciones: El valor de valor de entrada debe ser un número entero

    #Definición de las variables a emplear
    a = 0
    b = 1

    #Se comprueba que el valor de entrada es un número entero
    #Si el valor no es un número, entonces se le dice al usuario que el valor es incorrecto y que vuelva a probarlo.
    #En caso de que no, pues se ejecuta el algoritmo

    if isinstance(numero, numbers.Number):
        print("es un numero")

        while a < numero:
                print(a, end="")
                a = b
                b = a + b

                #Valores de salida
                print()
            
        print("de puta madre")
    
    else:
        print("no es número")




fib(10000)
#Precondiciones
#El parámetro que va a recibir la función, debe ser numérico.



#Algoritmo
#precondiciones
#postcondiciones