from modulo_1 import *
from modulo_2 import *
from subpaquete.modulo_3 import *

def lista_de_procesos():
    print("Suma - 1")
    print("Resta - 2")
    print("Multiplicacion - 3")
    print("Division - 4")
    print("Factorial - 5")
    print("Comprobacion numero primo - 6 ")


lista_de_procesos()
print(" ")
while True:
    print(" ")
    pregunta = input("Desea realizar algun proceso? si/no: ").capitalize()

    if pregunta == "Si":
        proceso=int(input("Ingresa el proceso que deseas realizar: "))
        print(" ")
        match proceso:
            case 1:
                print("Elegiste Suma.")
                suma=suma()
                print("el resultado es: " +str(suma)) #se uso el metodo "+ str()" para concatenar los numeros debido a que no me permitia usar "f"
            case 2:
                print("Elegiste Resta.")
                resta=resta()
                print("el resultado es: " +str(resta))
            case 3:
                print("Elegiste Multiplicación.")
                multiplicacion=multiplicación()
                print("el resultado es: " +str(multiplicacion))
            case 4:
                print("Elegiste Division.")
                division=división()
                print("el resultado es: " +str(division))
            case 5:
                print("Elegiste Factorial.")
                factorial=factorial()
                print("el factorial del numero ingresado es: " + str(factorial))
            case 6:
                print("Elegiste Comprobacion numero primo.")
                es_primo=es_primo()
                print(es_primo)
            case _:
                print("Numero invalido")
    else:
        break

