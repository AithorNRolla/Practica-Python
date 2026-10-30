cursos=["Java","Python","Typescript","C","Dart"]
#Pregunta al usuario que lenguaje quiere aprender.
#El programa le indicará si existe un curso o no. 

lenguaje=input("¿Qué lenguaje quieres aprender?")
"""""
encontrado=False
for c in cursos:
    if c==lenguaje:
        print("Tengo ese curso!")
        break
if not encontrado:
    print("Lo siente, no lo tengo.")

if lenguaje in cursos: 
    print("Tengo ese curso!")
else:
    print("Lo siente, no tengo ese curso.")
"""
if lenguaje.lower() in [c.lower() for c in cursos]:
    print("Tengo ese curso")
else:
    print("No lo tengo")
    
#El ejercicio es una chorrada de lo sencillo que es, pero he fallado en esto -pero no en lo elaborado-. 