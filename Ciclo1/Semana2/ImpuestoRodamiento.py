'''
El pago del impuesto de rodamiento de un vehículo se calcula de la siguiente manera:
 Se obtiene el 1% del avalúo del vehículo
 Se agrega un porcentaje sobre el anterior valor para las rentas municipales
 Se agrega un valor por Semaforización
 Si se paga antes de una fecha determinada, hay un descuento del 10%
 Después de esa fecha, hay otra de plazo para pagar sin multa ni intereses
 Después de esa fecha se aplica una multa e intereses mensuales de mora

'''
from datetime import date

#Datos entrada
avaluoVehiculo = float(input("Ingresar el avaluo del vehiculo: "))
porcentajeRentasMunicipales = float(input("Ingresar el porcentaje de rentas: "))
valorSemaforizacion = float(input("Ingresar el valor de semaforización: "))
valorMulta = float(input("Ingresar el valor de multa: "))
tasaInteresMensual = float(input("Ingresar la tasa de interés mensual: "))

print("Fecha Plazo con descuento")
print("Mes: 1.Ene 2.Feb 3.Mar 4.Abr 5.May 6.Jun 7.Jul 8.Ago 9.Sep 10.Oct 11.Nov 12.Dic")
mesFechaPagoDescuento = int(input("Escriba el mes: "))
diaFechaPagoDescuento = int(input("Escriba el día: "))

print("Fecha Plazo final")
print("Mes: 1.Ene 2.Feb 3.Mar 4.Abr 5.May 6.Jun 7.Jul 8.Ago 9.Sep 10.Oct 11.Nov 12.Dic")
mesFechaPlazoFinal = int(input("Escriba el mes: "))
diaFechaPlazoFinal = int(input("Escriba el día: "))

print("Fecha Pago")
print("Mes: 1.Ene 2.Feb 3.Mar 4.Abr 5.May 6.Jun 7.Jul 8.Ago 9.Sep 10.Oct 11.Nov 12.Dic")
mesFechaPago = int(input("Escriba el mes: "))
diaFechaPago = int(input("Escriba el día: "))


fechaPagoDescuento = date(date.today().year, mesFechaPagoDescuento, diaFechaPagoDescuento)
fechaPlazoFinal = date(date.today().year, mesFechaPlazoFinal, diaFechaPlazoFinal)
fechaPago = date(date.today().year, mesFechaPago, diaFechaPago)


valorImpuesto = avaluoVehiculo * 0.01
valorImpuesto = valorImpuesto * (1 + porcentajeRentasMunicipales/100) + valorSemaforizacion

if fechaPago <= fechaPagoDescuento:
    valorImpuesto = valorImpuesto * 0.9
else:
    if fechaPago > fechaPlazoFinal:
        diferenciaMes = (fechaPago - fechaPlazoFinal).days / 30
        valorImpuesto = valorImpuesto * (1 + diferenciaMes * tasaInteresMensual/100) + valorMulta

print("El valor del impuesto es: ", valorImpuesto)


'''
print("El Valor del Impuesto es: " , valorImpuesto)
print("El porcentaje de rentas es: " , porcentajeRentasMunicipales)
print("El avaluo del vehiculo es: " , avaluoVehiculo)
'''

