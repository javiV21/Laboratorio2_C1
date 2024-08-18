"""
Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa que
lea la información básica del perro (no más de 8 características) y se muestre en pantalla. En esta
veterinaria todos los animales que llegan, entran con el estado inicial de NO ATENDIDO y cuando se registran
se cambia automáticamente a ATENDIDO. Por ahora como la veterinaria solo atiende perros, basado en el peso
(menos de 10kg o más de 10kg) los registra como "Perro Grande" o "Perro Pequeño".
"""

class Veterinaria():
    # Creé los atributos que se calculan (tamaño) y actualizan (estado)
    # automáticamente, fuera de la función constructor (__init__).
    estado = "NO ATENDIDO"
    tamanio = ""
    
    # Asigné valores a los parámetros para poder crear la función
    # RecibirDatos() y no pasarle parámetros a la instancia.
    def __init__(self, nombre="", raza="", sexo="", edad="", peso=0, tratamiento="", duenio="", celDuenio=""):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.peso = peso
        self.tratamiento = tratamiento
        self.duenio = duenio
        self.celDuenio = celDuenio

    # Función para actualizar estado.
    def Registro(self):
        self.estado = "ATENDIDO"
        return self.estado
    
    # Función para calcular tamaño.
    def CalcTamanio(self):
        if (self.peso < 10):
            self.tamanio = "Perro pequeño"
        else:
            self.tamanio = "Perro grande"
        return self.tamanio
    
    # Función para recibir datos.
    def RecibirDatos(self):
        try:
            print("-----------------------")
            print("| CLÍNICA VETERINARIA |")
            print("-----------------------")
            print()
            print("Datos de tu mascota.")
            self.nombre = input("¿Cómo se llama el perro? ")
            print(f"Ingresa los siguientes datos de {self.nombre}.")
            self.raza = input("Raza: ")
            self.sexo = input("Sexo: ")
            self.edad = input("Años de edad: ")
            self.peso = int(input("Peso (kg): "))
            while (self.peso <= 0):
                print("Ingresa un peso válido.")
                self.peso = int(input("Peso (kg): "))
            self.tratamiento = input("Tratamientos: ")
            print()
            print("Ahora ingresa los siguientes datos de la persona responsable...")
            self.duenio = input("Nombre: ")
            self.celDuenio = input("Número de teléfono: ")
            
            # Luego de recibir los datos, envié los valores necesarios
            # para calcular tamaño y actualizar estado.
            self.Registro()
            self.CalcTamanio()
        # Manejé una excepción, por si se ingresan caracteres inválidos
        # en el atributo peso.
        except ValueError:
            print("************************************")
            print("¡Error! El peso debe ser ingresado\nusando únicamente valores numéricos.")
            print("************************************")
            print("Por favor, vuelve a empezar.")

    # Función para mostrar datos.
    def MostrarDatos(self):
        # Únicamente mostrará los datos si no hubo error en la entrada de estos.
        if (self.peso):
            print()
            print("  CLÍNICA VETERINARIA")
            print("-----------------------")
            print("| DATOS DE LA MASCOTA |")
            print("-----------------------")
            print(f"Nombre: {self.nombre}")
            print(f"Raza: {self.raza}")
            print(f"Sexo: {self.sexo}")
            print(f"Edad: {self.edad}")
            print(f"Peso: {self.peso}")
            print(f"Tamaño: {self.tamanio}")
            print(f"Tratamiento: {self.tratamiento}")
            print(f"Estado: {self.estado}")
            print()
            print("-------------")
            print("| ENCARGADO |")
            print("-------------")
            print(f"Dueño: {self.duenio}")
            print(f"Contacto: {self.celDuenio}")
            print("------------------")

# Creé la instancia y llamé los métodos
# para la entrada e impresión de datos.
perro1 = Veterinaria()
perro1.RecibirDatos()
perro1.MostrarDatos()