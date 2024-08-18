"""
Un grupo de mariachi con sede en San Miguel hace sus contratos por horas y en cada hora se tocan 12 canciones.
El precio varía en base al horario. Si es de 06:00 a 20:59, se cobra (por cada hora) $190 por la primera y por 2 o
más descuenta un 5% a cada hora. Si es de 21:00 a 05:59 se suman $10 a cada una. Además, se toma en cuenta el precio
del transporte (para ambos horarios), que si es en la misma ciudad, se cobran $10 y si es fuera, se cobran $10 + $0.5
por cada km de distancia (desde la ciudad hasta el lugar del evento). Se requiere de un programa que solicite al menos
5 datos del contrato y los presente al administrador del sistema; debe incluir los datos que se calculan automáticamente.
El programa calcula el precio en base al horario seleccionado (diurno/nocturno), no evalúa iniciar en uno y terminar en otro.
"""

class Mariachi():
    # Creé los valores que se calculan, fuera del constructor.
    precioHora = 0
    transporte = 10
    precioTotal = 0
    canciones = 12

    # Creé el constructor, asignandole valores a los parámetros, para manejar la entrada de datos
    # en la función RecibirDatos().
    def __init__(self, nombreC="", contacto="", horario=0, hora=0, horas=0, ciudad="", distancia=0):
        self.nombreC = nombreC
        self.contactoC = contacto
        self.horario = horario
        self.horaEvento = hora
        self.cantHoras = horas
        self.ciudad = ciudad
        self.distancia = distancia

    # Función para calcular el precio del transporte. Si la ciudad donde será el evento
    # es diferente a 'San Miguel' hará el cálculo respectivo, de lo contrario el transporte
    # tendrá el valor por defecto ($10)
    def Transporte(self):
        if (self.ciudad != "San Miguel"):
            self.transporte += (0.5 * self.distancia)
        return self.transporte
        
    # Función para definir si es horario diurno o nocturno y asignar el precio respectivo
    # al precioHora.
    def PrecioHorario(self):
        if (self.horario == 1):
            self.precioHora = 190
        elif (self.horario == 2):
            self.precioHora = 200
        return self.precioHora
        
    # Función para hacer el descuento del 5% a cada hora, si cantHoras es mayor que 1.
    def PrecioHoras(self):
        if (self.cantHoras > 1):
            self.precioHora -= (0.05 * self.precioHora)
        return round(self.precioHora,2)
        
    # Función para calcular el precio total, tomando en cuenta el precioHora, cantHoras y transporte.
    def PrecioTotal(self):
        self.precioTotal = (self.precioHora * self.cantHoras) + self.transporte
        return round(self.precioTotal,2)
    
    # Función para calcular el número de canciones (12 por cada hora).
    def Canciones(self):
        self.canciones *= self.cantHoras
        return int(round(self.canciones,0))
    
    # Creé RecibirDatos() para realizar la entrada de datos.
    def RecibirDatos(self):
        try:
            print("------------------------")
            print("| CONTRATO DE MARIACHI |")
            print("------------------------")
            print()
            print("Ingresa los siguientes datos del contrato que deseas registrar.")
            self.nombreC = input("Nombre del cliente: ") 
            self.contacto = input(f"Número de teléfono de {self.nombreC}: ")
            print("A continuación, ingresa el número (0/1) que acompaña\nal horario que tiene el contrato.")
            print("1-Diurno (06:00 - 20:59)")
            print("2-Nocturno (21:00 - 05:59)")
            self.horario = round(float(input("Número -> ")),0)
            # Si ingresa un valor diferente a 1 y 2 volverá a pedir el dato.
            while (self.horario != 1 and self.horario != 2):
                print("Para escoger un horario, selecciona '1' o '2'.")
                self.horario = round(float(input("Número -> ")),0)
            # Envié los valores respectivos para determinar el precio por la primera hora.
            self.PrecioHorario()
            self.cantHoras = float(input("Cantidad de horas: "))
            # Justifiqué que no pueden realizarse menos de 1 hora.
            while (self.cantHoras < 1):
                print("Ingresa una cantidad de horas válidas (1 o más).")
                self.cantHoras = float(input("Cantidad de horas: "))
            self.horaEvento = input("Hora de inicio (hh:mm): ")
            self.ciudad = input("Escribe la ciudad del evento: ").title()
            # Si la ciudad es San Miguel, no pedirá la distancia.
            if (self.ciudad != "San Miguel"):
                self.distancia = float(input(f"Distancia (km) de San Miguel a {self.ciudad}: "))
        # Manejé una excepción en caso de que se ingresen algunos valores incorrectos.
        except ValueError:
            print("****************************************************")
            print("¡Error! Debes ingresar únicamente valores numéricos.")
            print("****************************************************")
            print("Por favor, vuelve a empezar.")
    
    # Función para mostrar los datos.
    def MostrarDatos(self):
        # Solo se imprimirán si no hubo error   Incluye distancia = 0 para los casos en los
        # en la entrada de datos.               que la ciudad es 'San Miguel'.
        if (self.horario and self.cantHoras and (self.distancia == 0 or self.distancia)):
            print()
            print("----------------------")
            print("| DATOS DEL CONTRATO |")
            print("----------------------")
            print()
            print(f"Nombre del cliente: {self.nombreC}")
            print(f"Número de contacto: {self.contacto}")
            print()
            # Revisa el horario seleccionado.
            if (self.horario == 1):
                print("Horario: diurno")
            else:
                print("Horario: nocturno")
            print(f"Cantidad de horas: {self.cantHoras}")
            print(f"Hora de inicio: {self.horaEvento}")
            print(f"Canciones: {self.Canciones()}")
            print(f"Ciudad: {self.ciudad}")
            # Imprimirá la distancia solo si la ciudad no es 'San Miguel'.
            if (self.ciudad != "San Miguel"):
                print(f"Distancia: {self.distancia} km")
            print(f"Transporte: ${self.Transporte()}")
            print(f"Precio por hora: ${self.PrecioHoras()}")
            print(f"Total contrato: ${self.PrecioTotal()}")

# Creé la instancia y llamé los métodos
# para la entrada e impresión de datos.
contrato1 = Mariachi()
contrato1.RecibirDatos()
contrato1.MostrarDatos()