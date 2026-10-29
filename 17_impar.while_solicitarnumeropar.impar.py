#Se solicita la inserción de un número y el programa nos dirá
#si es par o impar. Después, se pregunta si quiere introducir otro número
#Si dice que si (S), se vuelve a pedir el número y a indicar si es par
#A continuación se vuelve a preguntar si quiere introducir otro número
#que diga que no (N)

resp="S"
while resp=="S" or resp=="S":
     num=int(input("Inserte un número"))
     if num%2==0:
      print("Par")
     else:
      print("Impar")
     resp=input("¿Añadimos otro número?")
     
     
     #Aquí la pregunta sería "¿Añadimos otro número S/N?"
     #COPIA DE LO QUE ME EXPONE LA IA AL METER MÍ CÓDIGO:
     # resp = "S"
# Usamos .upper() para convertir la respuesta a mayúscula automáticamente
#while resp.upper() == "S":
    #num = int(input("Inserte un número: "))
    #if num % 2 == 0:
     #   print("Par")
    #else:
     #   print("Impar")
    #resp = input("¿Añadimos otro número? (S/N): ")


    