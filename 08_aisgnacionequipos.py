#Teniendo en cuenta que alevín es 10 años y benjamín es 16.
#Hacer un programa que solicite la edad y nos muestre a que grupo pertenece. 
#Pertenece (el más cercano a su edad).
#La edad debe de estar entre los 9 y los 18 años. 
#Usar if.


edad=int(input("Introduce tu edad  "))

limite_inf,limite_sup,benjamin,alevin=9,18,10,16

if edad<limite_inf or edad>limite_sup:
    print("La edad no es válida")
else:
    distancia_benjamin=edad-benjamin
    distancia_alevin=alevin-edad
    if distancia_benjamin<distancia_alevin:
        print("Eres benjamin")
    else:
        print("Eres alevin")