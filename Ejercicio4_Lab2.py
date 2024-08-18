"""
Un almacén vende dispositivos electrónicos (celulares, tablets y portátiles). Todos PHR que es una nueva
marca que está entrando en el mercado. Se requiere almacenar sus 6 principales características. Todos son
productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde
a su margen de ganancia.
"""

class Almacen():
    # Creé dos constantes y dos valores calculables fuera del constructor.
    MARCA = "PHR"
    ORIGEN = "Importado"
    precioVenta = 0
    ganancia = 0

    # Creé el constructor de la clase e inicialicé los parámetros para realizar la
    # inserción de datos por medio de la función RecibirDatos().
    def __init__(self, prod="", color="", almacenamiento=0, so="", garantia="", precio=0):
        self.producto = prod
        self.color = color
        self.almacenamiento = almacenamiento
        self.so = so
        self.garantia = garantia
        self.precioCompra = precio

    # Función para definir producto.
    def Producto(self):
        if (self.producto == "1"):
            self.producto = "Celular"
        elif (self.producto == "2"):
            self.producto = "Tablet"
        elif (self.producto == "3"):
            self.producto = "Portátil"
        return self.producto
    
    # Función para definir almacenamiento. Si es 4 no lo evalúa,
    # pues el atributo guardará el valor automáticamente.
    def Almacenamiento(self):
        if (self.almacenamiento == "1"):
            self.almacenamiento = "64"
        elif (self.almacenamiento == "2"):
            self.almacenamiento = "128"
        elif (self.almacenamiento == "3"):
            self.almacenamiento = "256"
        return self.almacenamiento

    # Función para calcular precio de venta.
    def CalcPrecioV(self):
        self.precioVenta = 1.7 * self.precioCompra
        return round(self.precioVenta,2)
    
    # Función para calcular la ganancia por producto.
    def CalcGanancia(self):
        self.ganancia = self.precioVenta - self.precioCompra
        return round(self.ganancia,2)
    
    # Función para recibir datos.
    def RecibirDatos(self):
        try:
            print("-------------------------------------")
            print("| ALMACÉN DE PRODUCTOS ELECTRÓNICOS |")
            print("-------------------------------------")
            print()
            print("Selecciona el número que acompaña al producto que deseas registrar.")
            self.producto = input("1-Celular.\n2-Tablet.\n3-Portátil.\nNúmero -> ")
            # Los siguientes 2 while se repiten mientras no se ingrese un valor válido.
            while (self.producto not in ["1", "2", "3"]):
                print("Ingresa un valor válido.")
                self.producto = input("1-Celular.\n2-Tablet.\n3-Portátil.\nNúmero -> ")
            print(f"A continuación, ingresa los siguientes datos de {self.Producto()}")
            self.color = input(f"Color: ")
            print("Almacenamiento (selecciona el número de la izquierda que acompaña al valor correspondiente).")
            print("1-64 GB.\n2-128 GB.\n3-256 GB.\n4-Otro.")
            self.almacenamiento = input("Número -> ")
            while (self.almacenamiento not in ["1", "2", "3", "4"]):
                print("Ingresa un valor válido (entre 1 y 4).")
                print("1-64 GB.\n2-128 GB.\n3-256 GB.\n4-Otro.")
                self.almacenamiento = input("Número -> ")
            # El if está de manera alternativa, por si se selecciona la opción "Otro".
            if (self.almacenamiento == "4"):
                self.almacenamiento = input("Ingresa el almacenamiento (en GB): ")
            self.so = input("Sistema operativo: ")
            self.garantia = input("Tiempo de garantía (a partir de la venta): ")
            self.precioCompra = float(input("Precio de compra: $"))
            # Se repite mientras el valor ingresado sea menor o igual a 0.
            while (self.precioCompra <= 0):
                print("Ingresa un precio válido (mayor que 0).")
                self.precioCompra = float(input("Precio de compra: $"))
        # Excepción por si se ingresa un valor que genera error.
        except ValueError:
            print("********************************************************")
            print("Error: ingreso de datos incorrecto.\nPor favor, vuelve a empezar e ingresa únicamente\n"
                  "valores numéricos para el precio de compra del producto.")
            print("********************************************************")

    # Función para mostrar datos.
    def MostrarDatos(self):
        # Solo presentará la información si no hubo problema con los datos dentro de la condición if.
        if (self.precioCompra):
            print()
            print("-------------------------------------")
            print("| ALMACÉN DE PRODUCTOS ELECTRÓNICOS |")
            print("-------------------------------------")
            print()
            print("***Datos del producto registrado***")
            print(f"Producto: {self.Producto()}")
            print(f"Marca: {self.MARCA}")
            print(f"Origen: {self.ORIGEN}")
            print(f"Color: {self.color}")
            print(f"Capacidad de almacenamiento: {self.Almacenamiento()} GB")
            print(f"Sistema operativo: {self.so}")
            print(f"Garantía: {self.garantia}")
            print(f"Precio de compra: ${self.precioCompra}")
            print(f"Precio de venta: ${self.CalcPrecioV()}")
            print(f"Ganancia por producto: ${self.CalcGanancia()}")

# Creé la instancia y llamé los métodos
# para la entrada e impresión de datos.
producto1 = Almacen()
producto1.RecibirDatos()
producto1.MostrarDatos()