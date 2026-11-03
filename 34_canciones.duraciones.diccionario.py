#Lista de reproducción musical. 

lista_reproduccion=[
    {"titulo":"canción inventada","duración":3.20,"valoracion":4},
    {"titulo":"Bohemiam Rhapsody","duración":5.40,"valoracion":10},
    {"titulo":"Green Summer","duración":4.10,"valoracion":7}
]

#Se solicita la introducción de los datos de una nueva canción. 
#Si la canción no existe, se agrega a la lista. Si ya existe, no se hace nada. 
#Después, el programa muestra todos los títulos almacenados y la valoración media de todo. 
"""""
#Aquí vamos a pedir los datos de la canción:
nuevo_título=input("Introduce una nueva canción:  ")
nueva_duración=float(input("Introduce nueva duración:  "))
nueva_valoración=int(input("Introduce nueva valoración: "))
#Vamos a meter una cajita nueva para las canciones:
nueva_canción={
    "titulo": nuevo_título,
    "duración": nueva_duración,
    "valoración": nueva_valoración
}
lista_reproduccion.append(nueva_canción)
suma_valor=0
#Hacemos el bucle:
for cancion in lista_reproduccion:
    print(cancion["titulo"])
    duraciones=nueva_duración["duración"]
    nota_cancion=nueva_canción["valoración"]
    suma_valor=suma_valor+nota_cancion
total_canciones = len(lista_reproduccion)

media = suma_valor/total_canciones

print(f"La valoración media es: {media}")

"""
""""
título=input("Introduce una nueva canción:  ")
duración=float(input("Introduce nueva duración:  "))
valoración=int(input("Introduce nueva valoración: "))
cancion={"titulo":título,"duracion":duración,"valoracion":valoración}
"""
#Esto de arriba no está mal, solo que aquí abajo al hacer el bucle repito peticiones. 
#Algunas cosas las he reciclado como el .append() 

titulo_nuevo=input("Introduce una nueva canción:  ").strip()
ya_existe=False
for c in lista_reproduccion: #Aquí iniciamos el jodido bucle que tanto me ha dado por culo. 
    if c["titulo"].lower()==titulo_nuevo.lower():
        ya_existe=True 
if ya_existe==False:
    duración=float(input("Introduce nueva duración:  "))
    valoración=int(input("Introduce nueva valoración:  "))
    cancion={"titulo": titulo_nuevo, "duracion":duración,"valoracion":valoración,} #¡Al loro con las tildes!
    lista_reproduccion.append(cancion)
else:
 print("La canción ya existe y no se ha añadido")
suma=0
for c in lista_reproduccion:
    suma+=c["valoracion"]
    print(c["titulo"])
print(f"Valoración media {suma/len(lista_reproduccion)}")

#Podemos hacerlo también con una compresión de lista: 
"""
def comprobar_cancion(titulo):
    return titulo in [can["titulo] for can in lista_reproduccion]
"""
#Aquí se comprime todo, haciendo que la manera tradicional sea "extensa" en comparación. 