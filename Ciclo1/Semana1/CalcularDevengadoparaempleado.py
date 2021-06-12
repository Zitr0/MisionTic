#Calcular Devengado para empleado


salarioMensual = int(input("Ingrese salario basico: "))

valorHora = salarioMensual / 240
horasLaboradas = int(input("Ingrese las horas trabajadas, valor entero: "))
horasExtras = int(input("Ingrese las horas extras trabajadas, valor entero: "))
porcentajeExtras = int(input("Ingrese el porcentaje de la hora extra: "))

eps = 0.04 
afp = 0.04

valorHoraExtra = valorHora*(1+porcentajeExtras/100)
valorHorasLaboradas = (horasLaboradas * valorHora) + (valorHoraExtra * horasExtras)

saludPension = valorHorasLaboradas * (eps+afp) 

valorHorasLaboradas = valorHorasLaboradas - saludPension

print("El valor de las deducciones de salud y pensión son: ", saludPension)
print("Valor hora extras de este mes es: ",valorHoraExtra)
print("El salario devengado de este mes es: ",valorHorasLaboradas)


