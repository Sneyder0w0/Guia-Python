print("Ejercicio 6.1: Maneja excepciones en una división:")
print(" ")
# Escribe una función division_segura que reciba dos números,
def division_segura():
# realice la división y maneje correctamente las excepciones de:
    try:
        num1 = int(input("Ingrese el numero 1: "))
        num2 = int(input("Ingrese el numero 2: "))
        return num1/num2
    except (ZeroDivisionError,ValueError) as error: # - División por cero y Tipo de dato incorrecto (si se pasan valores no numéricos)
        print(f"El Error se debe a: {error}")
        
#testeo de funcion:
test=division_segura()  
print(test)

print(" ")
print("Ejercicio 6.2: Crea y lanza tus propias excepciones:")
# Crea una excepción personalizada EdadInvalidaError
class EdadInvalidaError(Exception):
    def __init__(self,edad):
        super().__init__(f"Edad inválida: {edad}. La edad debe ser mayor a 0 y menor a 120")

# Implementa una función verificar_edad que reciba una edad y:
def verificar_edad(edad):

# - Lance EdadInvalidaError si la edad es negativa o mayor a 120
    if edad < 0 or edad > 120:
        raise EdadInvalidaError(edad)
    
# - Devuelva True si la edad es válida
    else:
        return True
    
#testeo de la excepción/funcion
try:
    edad = int(input("Ingrese su edad: "))
    if verificar_edad(edad):
        print("Edad válida.")
except EdadInvalidaError as error:
    print(error)
