
valorPrestado = float(input("Monto a prestar? "))
tasa  = float(input("Tasa de interes? "))
plazo = float(input("Cuotas? "))

tasa = tasa / 100
x = (1 + tasa)**plazo
calcularCuota = round(valorPrestado * x * tasa / (x - 1))
valorFinal = round(calcularCuota * plazo)

print("================================")
print("Valor de la tasa:")
print(tasa)
print("Valor de la cuota:")
print(calcularCuota)
print("Valor del credito:")
print(valorFinal)
print("================================")