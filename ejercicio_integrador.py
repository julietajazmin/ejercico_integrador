""". Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos."""

class Cuenta:
    def __init__(self, titular, cantidad):
        """ titular: recibe solo string. Cantidad: recibe numeros 
        con decimales inclusive """
        self.titular = "" 
        self.cantidad = ""

    def settitular(self, titular):
        self.titular = titular

    def gettitular(self ):
        return self.titular
    
    def setcantidad (self, cantidad):
        self.cantidad = cantidad

    def getcantidad (self ):
        return self.cantidad


    def __str__(self):
        cadena= self.titular
        return cadena
    
    def __float__(self):
        float= self.cantidad
        return float
    
    def mostrar (self, titular, cantidad):
        self.titular = self.titular
        self.cantidad = self.cantidad

    def ingresar (self, Icantidad):

        if Icantidad > self.cantidad:
            print("El monto ingresado es negativo, intentelo nuevamente")

        else:
            """ continua normal"""

        self.cantidad = self.cantidad + Icantidad

    def retirar (self, Rcantidad):
        self.cantidad: self.cantidad - Rcantidad

"""8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta"""

class CuentaJoven (Cuenta):
    def __init__(self, cantidad, titular, bonificación, edad):
        self.bonificación = %
        self.edad = int

    def setbonificación(self, bonificación, edad):
        self.bonificación = bonificación
         
    def getbonificación(self ):
        return self.bonificación
    
    def setedad(self, edad):
        self.edad = edad
         
    def getedad(self ):
        return self.edad
    
    def es_titular_valido( edad ):
        if edad > 18:
            print("El titular es válido.")
        else:
            print("El titular es menor de edad.")
    
    def retirar
    def mostrar():
        print("Cuenta Joven", bonificación)