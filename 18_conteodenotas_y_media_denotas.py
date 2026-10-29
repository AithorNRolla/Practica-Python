#Solicita una nota, después otra, y así sucesivamente hasta introducir un cero
#en ese momento, no pedirá más notas y mostrará la nota media de las introducidas
#hasta el momento. 
"""""
sumar_notas=0
contador_notas=0

nota=int(input("Introduce una nota, introduce 0 para finalizar el conteo."))
while nota!=0:
 sumar_notas= sumar_notas+nota
 contador_notas= contador_notas+1
 nota=int(input("Introduzca otra nota, 0 para finalizar"))
 
if contador_notas > 0:
    media=sumar_notas/contador_notas
    print(f"La nota media de las notas es: {media}")
else:
    print("No se introdujeron las suficientes para hacer media")
"""

notas=0
sumas_notas=0

nota=int(input("Introduce un número de calificación, 0 para finalizar el conteo."))
while nota!=0:
    notas= notas+nota
    sumas_notas= sumas_notas+1
    nota=int(input("Introduce otra calificación, 0 para finalizar."))
    
if sumas_notas > 0:
    m=notas/sumas_notas
    print(f"La calificación media es: {m}")
else:
    print("No se introdujeron las suficientes calificaciones para hacer media")

#Este es la práctica mía paso a paso entendiendo cada mierda y qué significa, funciona. La de más arriba también. 

"""""
suma=0
total=0
nota=int(input("Introduce una nota"))
while nota>0:
    total=total+1
    suma=suma+nota
    nota=int(input("Introduce otra"))
    print(f"has introducido {total} notas, y la media es: {suma/total}")
"""
#Este de arriba es el del profesor, más sencillo. 