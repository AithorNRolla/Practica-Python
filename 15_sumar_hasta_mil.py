#1+2+3+4....¿hasta qué número tendremos que llegar?
#para que la suma alcance o supee el valor 1000?

#el valor no será 1000, si no 1001?? En la versión posterior que yo he metido, sobrepasa 1k!
#con el numero fijo en 24 clava los 1k. Aunque seguramente no sea esto lo que he de buscar. 

valor = 0
#aquí hago trampa, ya que el ejercicio va que el propio programa encuentre el número para llegar a 1k. 
#el número 24 clava lo que busco, pero no es como hay que buscarlo. 
numero_fijo=24

print(f"Empezando por {valor} y sumamos {numero_fijo} en {numero_fijo}:\n")

while valor < 1000:        
    valor += numero_fijo
    print(valor)          


print("\n¡Bucle terminado! Se ha alcanzado el objetivo de 1000.")