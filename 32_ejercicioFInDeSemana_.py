
cursos="Java basico, Python principiantes, C, Java avanzado, Java enterprise, python web, cobol"
"""
cursos=[{"nombre": "Python principiantes", "lenguaje":"Python", "nivel": "Principiante"}
        {"nombre": "Python web","lenguaje": "Python", "nivel": "web"}
        {"nombre": "Java basico","lenguaje": "Java", "nivel": "basico"}
        {"nombre": "Java avanzado","lenguaje": "Java", "nivel": "avanzado"}
        {"nombre": "Java enterpise","lenguaje": "Java", "nivel": "enterprise"}
        {"nombre": "C","lenguaje": "C"}{"nombre": "Cobol","lenguaje":"Cobol"}]
       
#Solicitamos al usuario que introduzca un lenguaje que quiere aprender, le mostramos todos los cursos
#relacionados con ese lenguaje. (Con las opciones que hay, algunas tienen más de una opción)

print=("Buscador de cursos")

busqueda=input("¿Qué lenguaje buscas?").strip().lower() #El ejercicio no está completo y no funciona. 
print(f"Resultados para {busqueda}:")
encontrado=False

for cursos in curso:
    if cursos["lenguaje"]==busqueda:
        print(F"{curso[nombre]}({curso[nivel]})")
        encontrado=True
    if not encontrado:
        print("No se encuentra el curso")
"""
lista_cursos=cursos.split(",") #El ejemplo del profesor, habrá que darle chicha a esto por que no lo termino de entender. 
lenguaje=input("Que lenguaje te interesa?")
for c in lista_cursos:
    if lenguaje.lower() in c.lower().split(" "):
        print(c)