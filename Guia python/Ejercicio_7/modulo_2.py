# - factorial

def factorial():
    num = int(input("Ingrese un numero del que desea obtener su factorial: "))
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    
    return resultado
