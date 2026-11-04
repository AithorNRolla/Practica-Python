cursos=[
    {"denominacion":"Python y datos","horario":"mañana","fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","horario":"mañana","fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","horario":"tarde","fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","horario":"festivos","fecha_fin":"30/09/2025"}  
] 
#se pide al usuario que introduzca horario
#les mostraremos los nombres de los cursos con ese horario. 
"""
horario=input("Introduce horario (mañana/tarde/festivos): ")

cursos_filtrados=list(filter(lambda c:c["horario"]==busqueda,cursos))
print("Lo cursos disponibles en ese horario son:  ")
for c in cursos_filtrados:
    print(f" - {c(["denominacion"])}")
"""

horario=input("Introduce el horario: ")
print(list(map(lambda l:l["denominacion"],
               filter(lambda c:c["horario"]==horario,cursos)))) 