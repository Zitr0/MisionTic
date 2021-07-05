#NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, sirven para probar tu código en consola, y el funcionamiento de la clase cliente
from pruebas import pruebas_codigo_estudiante
from cliente import cliente
"""NOTAS: 
    -PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
    -LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO
"""
def sede_bancaria(cola_general):
    cola_caja = list()
    cola_info = list()
    suma_retiros = 0
    suma_consignaciones = 0
    edad_minima_retiro = -1
    edad_minima_consignacion = -1
    edad_minima_info = -1
    for cliente in cola_general:
        if cliente.fila_interes == 'caja':
            cola_caja.append(cliente.nombre)
            if cliente.transaccion == 'retirar':
                suma_retiros += cliente.cantidad_retirar
                if edad_minima_retiro == -1 or edad_minima_retiro > cliente.edad:
                    edad_minima_retiro = cliente.edad
            elif cliente.transaccion == 'consignar':
                suma_consignaciones += cliente.cantidad_consignar
                if edad_minima_consignacion == -1 or edad_minima_consignacion > cliente.edad:
                    edad_minima_consignacion = cliente.edad
                
        else:
            cola_info.append(cliente.nombre)
            if edad_minima_info == -1 or edad_minima_info > cliente.edad:
                edad_minima_info = cliente.edad
                
    return cola_caja, cola_info, suma_retiros, suma_consignaciones, edad_minima_retiro, edad_minima_info, edad_minima_consignacion

"""
NO PEDIR DATOS CON LA FUNCIÓN input(), NO COLOCAR CÓDIGO FUERA DE LAS FUNCIONES QUE USTED CREE
Esta línea de código que sigue, permite probar si su ejercicio es correcto
Por favor NO ELIMINARLA, NO MODIFICARLA
"""
pruebas_codigo_estudiante(sede_bancaria)