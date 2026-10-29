notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#Indica cuantos alumnos han aprobado. (Debe de decir cuantos han aprobado, no los aprobados)

aprobados=0
suspensos=0

for num in notas_alumnos:
    if num>=5:
        aprobados=aprobados+1
    else:
        suspensos=suspensos+1
print(f"Han aprobado  ", aprobados)
for num in notas_alumnos:
    if num<=5:
        suspensos=suspensos+1
        
print(f"Han suspendido ", suspensos)
#Indica la nota más alta. 
nota_maxima=max(notas_alumnos)
print(f"La nota más alta es un {nota_maxima}")
#Indica la nota más baja.
nota_min=min(notas_alumnos)
print(f"La nota más baja es un {nota_min}")
#Mi forma de hacerlo desde mi punto de vista es más limpia. 