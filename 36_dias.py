dia=input("Dime un día de la semana ")
dias={"lunes","martes","miércoles"}
if dia in dias:
    print("ese día ya existe")
else:
    dias.add(dia)
print(dias)
lista_dias=list(dias)
print(lista_dias)