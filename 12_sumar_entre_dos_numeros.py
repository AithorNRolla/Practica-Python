#Solicita la introducción de dos números y calcula la suma de todos los números
#comprendidos entre el menor y el mayor.
"""
num1=int(input("Introduce el primer número  "))
num2=int(input("Introduce el segundo número  "))
suma=0

if num1<num2:
    menor=num1
    mayor=num2      
else:
    menor=num2
    mayor=num1
for nume in range(menor,mayor+ 1):
    suma=suma+num2

print("La suma es ",suma)
"""
#aquí arriba me esta dando errores, ya que no hace la suma (hemos probado algunas formas con la IA pero nah!)

num1=int(input("Primer número "))
num2=int(input("Segundo número "))
suma=0
#solución 1
if num1<num2:
    menor,mayor=num1,num2
else:
    menor=num2
    mayor=num1
    
for n in range(menor,mayor+1):
    suma=suma+n