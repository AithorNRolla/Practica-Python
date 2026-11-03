numeros=[3,-1,-9,4,2,11,-8,7,-5]
#Crea una lista a partir de la anterior que contenga
#solo los positivos
positivos=[]
"""
for n in numeros:
    if n>=0:
        positivos.append(n)
"""
positivos=[n for n in numeros if n>=0]
print(positivos)

#Indica si hay número par en la lista:
if [n for n in numeros if n%2==0]:
    print("Hay algun par")
else:
    print("No hay pares")