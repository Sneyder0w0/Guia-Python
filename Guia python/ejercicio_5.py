print("Ejercicio 5.1: Crea una clase Persona con atributos y métodos:")
class Persona:
# Implementa esta clase con:
# - Método constructor
    def __init__(self,nombre,edad,direccion):
        # - Atributos: nombre, edad, dirección
        self.nombre=nombre
        self.edad=edad
        self.direccion=direccion
    
# - Método __str__ para representación en cadena
    def __str__(self):
         return f"El nombre de la persona es: {self.nombre}, tiene {self.edad} de edad y su direccion es {self.direccion}"
# - Método cumplir_años que incremente la edad en 1
    def cumplir_años(self):
        self.edad += 1
# - Método cambiar_direccion que actualice la dirección
    def cambiar_dirección(self,n_direccion):
        self.direccion = n_direccion

print(" ")
print("Ejercicio 5.2: Implementa herencia entre clases:")
# Crea una clase Estudiante que herede de Persona y añada:
class Estudiante(Persona):
    def __init__(self,nombre,edad,direccion,curso): 
        super().__init__(nombre,edad,direccion)
        # - Atributo: curso
        self.curso=curso
# - Método: cambiar_curso
    def cambiar_curso(self,n_curso):
        self.curso = n_curso
# - Sobrecarga del método __str__ para incluir el curso
    def __str__(self):
            return f"El nombre de la persona es: {self.nombre}, tiene {self.edad} de edad, su direccion es {self.direccion} y está en el curso {self.curso}"

#testeo en clase "hija"
nombre=input("Añade tu nombre: ")
edad=int(input("Añade tu edad: "))
direccion=input("Ingresa tu direccion: ")
curso=input("Ingrese su curso: ")

test = Estudiante(nombre, edad,direccion,curso)
print(test)

while True:
    preguntar = input("Estas cumpliendo años? si / no: ").capitalize()
    if preguntar=="Si":
        print(" ")
        test.cumplir_años()
        print("Feliz cumpleaños! Tus datos fueron actualizados con tu nueva edad!")
        print(" ")
        print(test)
    else:
        print(" ")
        break

while True:
    preguntar = input("Desea cambiar la direccion? si/no: ").capitalize()
    if preguntar=="Si":
        print(" ")
        n_direccion=input("Añada la nueva dirección: ")
        test.cambiar_dirección(n_direccion)
        print("Direccion cambiada exitosamente!")
        print(" ")
        print(test)
    else:
        print(" ")
        break

