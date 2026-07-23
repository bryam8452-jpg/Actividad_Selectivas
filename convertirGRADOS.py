celcius = float(input("Temperartura en °C: "))
print("1. Fahrenheit\n2. Kelvin")
opcion = int(input("Elige opcion : "))
match opcion:
    case 1:
        resultado = celcius * 9/5 + 32
        unidad = "°F"
    case 2:
         resultado = celcius + 273.15
         unidad =  "°K"
    case _:
        resultado = None
        print("Opcion invalida")
if resultado is not None:
    print("Convertido: ", resultado, unidad)