import functools as ft 
numeros=[1,8,3,-4,9,-2,-11,16]
positivos=list(filter(lambda n:n>0,numeros))
print(positivos)
#Calcula la suma de los cuadrados de todos los positivos:
print(ft.reduce(lambda a,b:a+b,map(lambda n:n**2, positivos)))