#Solicitar la introducción de números, uno a uno. 
#Los guardamos en una lista
#Después de pedir un número, pregunta si quiere introducir otro, si dice si(S), pide uno nuevo
#Y así sucesivamente hasta que diga que no (N).
#Al final, muestra la lista completa. 

lista_numeros=[]
continuar= "S"

while continuar.upper()=="S":
    try:
        num=int(input("Introduce un número  "))
        lista_numeros.append(lista_numeros)
        continuar=input("¿Deseas introducir otro S/N?  ")
#He usado "upper" pero el profesor no lo ha explicado. 
#Append funciona, aunque no termino de entender del todo. 
    except ValueError:
     print("Error, número no válido, reintroduce un número correcto")
    #Try va de la mano con Except, la posición debe de coincidir!