# - es_primo (que determine si un número es primo)
def es_primo():
    num= int(input("Ingrese un numero para determinar si es primo o no: "))

    for i in range(2, num):
        if num % i == 0:
            return("No es primo") 
        else:
            return "El numero es primo"

