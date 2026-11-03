dia=input("Dime un día de la semana ")
dias={"lunes","martes","miércoles"}
if dia in dias:
    print("ese día ya existe")
else:
    dias.add(dia)
print(dias)
lista_dias=list(dias)
print(lista_dias)

lista_numeros=[4,7,11,3,2,11,9,4,7]
conjunto_numeros=set(lista_numeros)
print(conjunto_numeros) #Esto nos ayudará a quita duplicados. 