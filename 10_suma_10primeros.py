#Hacer un programa que muestre la suma de todos números. 
#Números naturales del 1 y un número leído por teclado. 

suma=0
limite=int(input("Introduce límite"))
for num in range(1,límite+1):
     suma=suma+num
print("La suma de los números es: ",suma)
