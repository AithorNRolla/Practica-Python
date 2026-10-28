#Lee la nota de un alumno y dependiendo del número (0 - 10)
#le indica si es suspenso (menos de 5), aprobado (5 o 6),
#notable (7 o 8) o sobresaliente (9 o 10)

nota=int(input("Introduce la nota  "))
suspenso= 0 and 4
aprobado= 5 and 6
notable= 7 and 8
sobresaliente= 9 and 10
match nota:
    case 1|2|3|4:
        print("Supenso")
    case 5|6:
        print("Aprobado")
    case 7|8:
        print("Notable")
    case 9|10:
        print("Sobresaliente")