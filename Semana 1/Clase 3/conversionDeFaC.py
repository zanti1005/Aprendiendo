#paso 1: pedir los °F
valorFahrenheit = int(input("Por favor ingrese eñ valor en F: "))

#paso 2: aplicar fórmula de conversión entre F y °C
valorCentigrados = (valorFahrenheit -32) * 5/9

#paso 3: mostrar el resultado
print(f"El valor en Centígrados es: {valorCentigrados}")
