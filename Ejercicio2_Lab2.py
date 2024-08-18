"""
Una papelería vende cuadernos y lápices. Los cuadernos pueden ser de 50 hojas o de 100 hojas. Los lápices
pueden ser de grafito o de colores. El precio de venta es igual al precio de compra multiplicado por 1.30
que corresponde al margen de ganancia. La papelería requiere construir un programa que le permita registrar
y visualizar por lo menos dos artículos de ítem. Todos los cuadernos son marca HOJITAS y los lápices son
marca RAYAS ya que la papelería es un distribuidor exclusivo.
"""

class Papeleria():
    # Creé 2 constantes y 3 atributos calculables.
    MARCA_CU = "HOJITAS"
    MARCA_LA = "RAYAS"
    prod = ""
    precioVenta = 0
    ganancia = 0

    # Asigné valores a los parámetros para poder crear la función
    # RecibirDatos() y no pasarle parámetros a la instancia.
    def __init__(self, producto=0, precioComP=0):
        self.producto = producto
        self.precioComp = precioComP

    # Función para calcular el precio de venta.
    def PrecioVenta(self):
        self.precioVenta = self.precioComp * 1.30
        return round(self.precioVenta,2)
    
    # Función para calcular la ganancia por producto.
    def CalcGanancia(self):
        self.ganancia = self.precioVenta - self.precioComp
        return round(self.ganancia,2)

    # Función para definir qué producto se seleccionó.
    def Producto(self):
        if (self.producto == 1):
            self.prod = "Cuaderno de 50 hojas"
        elif (self.producto == 2):
            self.prod = "Cuaderno de 100 hojas"
        elif (self.producto == 3):
            self.prod = "Lápiz de grafito"
        elif (self.producto == 4):
            self.prod = "Lápiz de color"
        return self.prod

    # Función para recibir datos.
    def RecibirDatos(self):
        try:
            print("-------------")
            print("| PAPELERÍA |")
            print("-------------")
            print()
            print("Selecciona el número del producto que deseas registrar.")
            print("1-Cuaderno de 50 hojas.\n"
                +"2-Cuaderno de 100 hojas.\n"
                +"3-Lápiz de grafito.\n"
                +"4-Lápiz de color.")
            self.producto = int(input("Número -> "))
            #Bucle para asegurarse que se ingrese un valor entre 1 y 4.
            while (self.producto not in [1, 2, 3, 4]):
                print("Para escoger un producto, ingresa un valor entre 1 y 4.")
                self.producto = int(input())
            self.Producto()
            self.precioComp = float(input(f"Ingresa el precio de compra del producto '{self.prod}': $"))
            # Luego de recibir los datos, envié los valores necesarios
            # para calcular el precio de venta y la ganancia por producto.
            self.PrecioVenta()
            self.CalcGanancia()
        # Manejé una excepción, por si se ingresan caracteres inválidos
        # en el atributo precioComp.
        except ValueError:
            print("Error: ingreso de valores no válidos.\n"
                  +"Por favor, vuelve a empezar e ingresa valores numéricos.")

    # Función para mostrar datos.
    def MostrarDatos(self):
        # Únicamente mostrará los datos si no hubo error en la entrada de estos.
        if (self.producto and self.precioComp):
            print()
            print(f"Producto registrado: {self.prod}.")
            # if para definir qué marca es el producto registrado.
            if (self.producto == 1 or self.producto == 2):
                print(f"Marca: {self.MARCA_CU}")
            elif (self.producto == 3 or self.producto == 4):
                print(f"Marca: {self.MARCA_LA}")
            print(f"Precio de compra: ${self.precioComp}")
            print(f"Precio de venta: ${self.precioVenta}")
            print(f"Ganancia del producto: ${self.ganancia}")

# Creé la lista productos para guardar cada producto registrado.
productos = []
# Creé una instancia para almacenar el primer producto registrado.
# Seguidamente llamé los métodos para entrada e impresión de datos.
producto = Papeleria()
producto.RecibirDatos()
# Agregué el primer producto a la lista con append()
productos.append(producto)
producto.MostrarDatos()

op = "s"
print()
# Creé un ciclo while para preguntar si quiere seguir registrando más.
# Este while se ejecutará automáicamente una vez debido a que se requiere
# registrar "al menos 2" productos.
print("A continuación, registra el segundo producto.")
while (op == "s"):
    # Una instancia para cada nuevo producto que se ingrese.
    producto = Papeleria()
    producto.RecibirDatos()
    productos.append(producto)
    producto.MostrarDatos()
    print()
    op = input("¿Deseas registrar otro producto? (s/n) ").lower()

print()
print()
print("*************************")
print("* PRODUCTOS REGISTRADOS *")
print("*************************")
# Muestro todos los productos que tiene la lista con un ciclo for.
for producto in productos:
    print("-------------------------")
    producto.MostrarDatos()
    print("-------------------------")