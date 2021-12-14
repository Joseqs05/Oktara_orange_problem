class Caja:
    numero = 0
    contenido = ''
    cantidadInicial = 0
    cantidadRestante = 0

    #Constructor de Caja
    def __init__(self, numero, contenido, cantidadInicial):
        self.numero = numero
        self.contenido = contenido
        self.cantidadInicial = cantidadInicial
        self.cantidadRestante = cantidadInicial

    #Se saca la cantidad solicitada de frutas, si es mayor al contenido se pregunta si se rellena la caja o no y se devuelve la cantidad que falta por 
    # sacar en la siguiente(s) caja(s)
    #Informa la cantidad que queda en la caja
    def sacarCantidad(self, cantidad):
        if self.cantidadRestante >= cantidad:
            self.cantidadRestante -= cantidad
            print(f'En la caja {self.numero} quedan {self.cantidadRestante}...')
            return 0
        else:
            faltantes = cantidad - self.cantidadRestante
            self.cantidadRestante = 0
            print(f'La caja {self.numero} ya esta vacia...')
            rellenar = input('Desea rellanar la caja? y/n ')
            if rellenar.lower() == 'y':
                self.rellenarCaja()
            return faltantes

    def rellenarCaja(self):
        self.contenido = 'Manzanas'
        self.cantidadRestante = self.cantidadInicial