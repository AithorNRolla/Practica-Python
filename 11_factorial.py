#Realizar un programa que solicite la introducción de un número
#y calcule su factorial 7! 7*6*5*4*3*2*1

factorial=1
límite=int(input("Introduce limite "))
for numero in range(2,limite+1):
    factorial=factorial*numero
print(f"El factorial de {limite} es: ",factorial) 
