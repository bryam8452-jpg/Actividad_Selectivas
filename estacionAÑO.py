mes = int(input("Numero de mes (1-12)"))
match mes:
    case 12 | 1 | 2:
        estacion = "invierno"
    case 3 | 4 | 5:
         estacion = "primavera"
    case 6 | 7 | 8:
         estacion = "verano"
    case 9 | 10 | 11:
        estacion = "otoño"     
    case _: 
        estacion = "Mes invalido"
print("Estacion: ", estacion)#verifica la estacion del año