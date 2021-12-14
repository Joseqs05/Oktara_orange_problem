from Caja import Caja

def main():
    #Menu incial, parametros para la configuracion de la tienda
    cantidadCajas = int(input('Cuantas cajas hay?: '))
    cantidadXCaja = int(input('Cuantas naranjas por caja hay?: '))
    precioXNaranja = int(input('Cuanto cuesta la naranja?: '))
    print('\n')

    tienda = []
    #inicializa la tienda
    for i in range(0,cantidadCajas):
        caja = Caja(i+1, 'Naranjas', cantidadXCaja)
        tienda.append(caja)

    #Selecciona la caja mas a la derecha para ir sacando las frutas
    cajaActual = cantidadCajas

    #proceso de venta
    while(True):
        #Caso en que se hayan vendido todas las frutas y se devuelve a usar la caja mas a la derecha
        if tienda[0].cantidadRestante == 0:
            tienda = rellenarCajas(tienda)
            cajaActual = cantidadCajas
            print('Las cajas se han rellando con manzanas!\n')

        cantidadAComprar = int(input('Cuantas unidades desea adquirir?: '))

        #Caso en que se trate de comprar mas de lo que hay
        if cantidadAComprar > determinarCantidadActual(tienda):
            print('La cantidad solicitada es mayor a la cantidad actual del producto... intente de nuevo!\n')
            return
        
        #Caso en que se compren mas frutas de las que hay en la caja y haya que pasarse de caja
        restantes = comprar(tienda, cajaActual, cantidadAComprar)

        while restantes > 0:
            cajaActual -= 1
            print(f'Pasando a caja {cajaActual}...\n')
            restantes = comprar(tienda, cajaActual, restantes)

        #Imprime el precio a pagar por la cantidad de frutas compradas 
        factura(cantidadAComprar, precioXNaranja)

        terminar = input('Desea terminar la simulacion? y/n: ')
        if terminar.lower() == 'y':
            break

def factura(cantidad, precio):
    print(f'El precio a pagar es de: ${cantidad * precio}\n')

#Rellena TODAS las cajas
def rellenarCajas(tienda):
    recargar = input('Las cajas estan completamente vacias, desea rellenar TODAS con Manzanas? y/n: ')
    if recargar.lower() == 'y':
        for caja in tienda:
            caja.rellenarCaja()
    return tienda

def determinarCantidadActual(tienda):
    quedan = 0
    for caja in tienda:
        quedan += caja.cantidadRestante
    return quedan

def comprar(tienda, caja, restantes):
    return tienda[caja-1].sacarCantidad(restantes)

main()