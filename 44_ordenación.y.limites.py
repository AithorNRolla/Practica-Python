lista=[5,2,11,6,44,20,1]
lista_ordenada=sorted(lista,reverse=True)
print(lista_ordenada)
nombres=["bicicleta","oro","casa","martillo"]
print(sorted(nombres))
#ordenación personalizada, por ejemplo por número de carácteres. 
print(sorted(nombres,key=lambda e:len(e)))