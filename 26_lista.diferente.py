#Dada esa lista de notas, crea otra lista 
#que contenga solo los aprobados, además añade un punto extra a cada uno. 
#Finalmente imprime la lista. 
#[8,9,8,10]

numeros=[4,3,7,8,7,9,2]
aprobados=[]
for nota in numeros: #Empieza igual que el ejercicio 20
    if nota>=5:
        aprobados.append(nota+1) #La diferencia es meter el append.
print(aprobados)
#-------------------------------------------------------
#-------------------------------------------------------
#-------------------------------------------------------
aprobados=[nota+1 for nota in numeros if nota>=5] #Esto es COMPRESIÓN DE LISTAS.
print(aprobados)
    
