"""
Un concesionario de autos vende vehículos nacionales e importados. Todos tienen 4 ruedas y capacidad para
5 pasajeros. Esta información debe registrarse siempre por razones de ley. Requiere un programa que le
permita almacenar las 10 principales características de los autos. El precio de venta de cada auto es
igual al precio de compra multiplicado por 1.4 que corresponde a su margen de ganancia.
"""

class Concesionario():
    # Creé dos constantes y dos valores calculables fuera del constructor.
    RUEDAS = 4
    CAP_PASAJEROS = 5
    precioVenta = 0
    ganancia = 0

    # Creé el constructor de la clase e inicialicé los parámetros para realizar la
    # inserción de datos por medio de la función RecibirDatos().
    def __init__(self, origenCompra="", marca="", modelo="", tipo="", precioCompra=0, anio="",
                 traccion="", transmision="", color="", combustible=""):
        self.origen = origenCompra
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.precioCompra = precioCompra
        self.anio = anio
        self.traccion = traccion
        self.transmision = transmision
        self.color = color
        self.combustible = combustible

    # Función para determinar si el auto fue adquirido
    # en el territorio nacional o si fue importado.
    def Origen(self):
        if (self.origen == "1"):
            self.origen = "Nacional"
        else:
            self.origen = "Importado"
        return self.origen
    
    # Función para determinar el tipo de tracción.
    def Traccion(self):
        if (self.traccion == "1"):
            self.traccion = "Delantera"
        elif (self.traccion == "2"):
            self.traccion = "Trasera"
        elif (self.traccion == "3"):
            self.traccion = "4x4"
        return self.traccion
    
    # Función para determinar el tipo de transmisión.
    def Transmision(self):
        if (self.transmision == "1"):
            self.transmision = "Manual"
        elif (self.transmision == "2"):
            self.transmision = "Automática"
        return self.transmision

    # Función para determinar el tipo de combustible.
    def Combustible(self):
        if (self.combustible == "1"):
            self.combustible = "Gasolina"
        elif (self.combustible == "2"):
            self.combustible = "Diesel"
        elif (self.combustible == "3"):
            self.combustible = "Eléctrico"
        return self.combustible

    # Función para calcular el precio de venta.
    def CalcPrecioV(self):
        self.precioVenta = self.precioCompra * 1.4
        return round(self.precioVenta,2)
    
    # Función para calcular la ganancia por auto.
    def CalcGanancia(self):
        self.ganancia = self.precioVenta - self.precioCompra
        return round(self.ganancia,2)
    
    # Función para recibir los datos.
    def RecibirDatos(self):
        try:
            print("--------------------------")
            print("| CONCESIONARIO DE AUTOS |")
            print("--------------------------")
            print()
            print("Ingresa los siguientes datos del auto que deseas registrar.")
            self.origen = input("El auto es:\n(1)-Nacional.\n(2)-Importado.\nIngresa 1 o 2 según sea el caso -> ")
            # Se repite mientras no se ingerse un valor válido.
            while (self.origen not in ["1", "2"]):
                print("Ingresa un valor válido (1 o 2).")
                self.origen = input("Número -> ")
            self.marca = input("Marca: ")
            self.modelo = input("Modelo: ")
            self.tipo = input("Tipo (sedan, pick up...): ")
            self.anio = input("Año de vehículo: ")
            self.color = input("Color de carrocería: ")
            # Los siguientes 3 while se repiten mientras no se ingrese un valor válido.
            # Los if están de manera alternativa, por si se selecciona la opción "Otro".
            self.traccion = input("Tracción (elige un número):\n1-Delantera\n2-Trasera\n3-4x4\n4-Otro\nNúmero -> ")
            while (self.traccion not in ["1", "2", "3", "4"]):
                self.traccion = input("Elige un valor válido (entre 1 y 4):\n"
                                        "1-Delantera\n2-Trasera\n3-4x4\n4-Otro\nNúmero -> ")
            if (self.traccion == "4"):
                self.traccion = input("Escribe el tipo de tracción: ")

            self.transmision = input("Transmisión (elige un número):\n1-Manual\n2-Automática\n3-Otro\nNúmero -> ")
            while (self.transmision not in ["1", "2", "3"]):
                self.transmision = input("Elige un valor válido (entre 1 y 3):\n"
                                        "1-Manual\n2-Automática\n3-Otro\nNúmero -> ")
            if (self.transmision == "3"):
                self.transmision = input("Escribe el tipo de transmisión: ")

            self.combustible = input("Tipo de combustible (selecciona el número que acompaña al tipo).\n"
                  "1-Gasolina\n2-Diesel\n3-Eléctrico\n4-Otro\nNúmero -> ")
            while (self.combustible not in ["1", "2", "3", "4"]):
                self.combustible = input("Selecciona un número entre 1 y 4.\n"
                    "1-Gasolina\n2-Diesel\n3-Eléctrico\n4-Otro\nNúmero -> ")
            if (self.combustible == "4"):
                self.combustible = input("Escribe el tipo de combustible: ")

            self.precioCompra = float(input("Precio de compra: $"))
            # Se repite mientras el valor ingresado sea menor o igual a 0.
            while (self.precioCompra <= 0):
                print("Ingresa un precio válido (mayor que 0).")
                self.precioCompra = float(input("Precio de compra: $"))
        # Excepción por si se ingresa un valor que genera error.
        except ValueError:
            print("****************************************************")
            print("¡Error! Debes ingresar únicamente valores numéricos.")
            print("****************************************************")
            print("Por favor, vuelve a empezar.")

    # Función para mostrar los datos.
    def MostrarDatos(self):
        # Solo presentará la información si no hubo problema con los datos dentro de la condición if.
        if (self.origen and self.precioCompra and self.traccion and self.transmision and self.combustible):
            print()
            print("--------------------------")
            print("| CONCESIONARIO DE AUTOS |")
            print("--------------------------")
            print()
            print("***Datos del automóvil***")
            print(f"Vehículo: {self.Origen()}")
            print(f"Marca: {self.marca}")
            print(f"Modelo: {self.modelo}")
            print(f"Tipo: {self.tipo}")
            print(f"Capacidad de pasajeros {self.CAP_PASAJEROS} personas")
            print(f"Ruedas: {self.RUEDAS}")
            print(f"Año: {self.anio}")
            print(f"Color de carrocería: {self.color}")
            print(f"Tracción: {self.Traccion()}")
            print(f"Transmisión: {self.Transmision()}")
            print(f"Combustible: {self.Combustible()}")
            print(f"Precio de compra: ${self.precioCompra}")
            print(f"Precio de venta: ${self.CalcPrecioV()}")
            print(f"Ganancia: ${self.CalcGanancia()}")

# Creé la instancia y llamé los métodos
# para la entrada e impresión de datos.
vehiculo1 = Concesionario()
vehiculo1.RecibirDatos()
vehiculo1.MostrarDatos()