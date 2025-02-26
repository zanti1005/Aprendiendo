#paso 1: pedir los °C
valorCentigrados = int(input("Por favor ingrese eñ valor en °C: "))

#paso 2: aplicar fórmula de conversión entre °C y F
valorFahrenheit = (valorCentigrados * 9/5) + 32

#paso 3: mostrar el resultado
print(f"El valor en Fahrenheit es: {valorFahrenheit}")
