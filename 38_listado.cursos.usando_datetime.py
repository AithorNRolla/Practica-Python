
#El ejemplo en azul de abajo funciona, pero es más extenso y no va con DEF. 
"""

 import datetime #AQUI FUNCIONA SIN DT. 
 
lista_cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador certificado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"10/03/2025"},
]
#Nombre del curso con la nota media más alta (¿la media también?)
#Nombre del curso que finalizó antes

#Necesitamos dos variables (Notas)
curso_antes=""
curso_top=0

#necesitaremos un "bucle" (Fechas)
curso_antiguo=""
fecha_antigua= None

#aquí empezamos el bucle:

for curso in lista_cursos:
    nota_maxima=max(curso["calificaciones"])
    fecha_curso_real=datetime.datetime.strptime(curso["fecha_fin"],"%d/%m/%Y")
    if nota_maxima>curso_top:
        curso_top=nota_maxima
        curso_antes=curso["denominacion"]
    if fecha_antigua==None or fecha_curso_real<fecha_antigua:
        fecha_antigua=fecha_curso_real
        curso_antiguo=curso["denominacion"]
print(f"El curso con la nota más alta es:  {curso_antes}(nota: {curso_top})")
print(f"El curso que terminó antes es: {curso_antiguo}")

"""
#Aquí vamos hacerlo diferente con los DEF:
"""""
import datetime as dt #si quiero usar DT tengo que ponerlo así: import datetime as dt. 
cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador certificado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"10/03/2025"},
]

def media(numeros):
    suma=0
    for n in numeros:
        suma+=n
    return suma/len(numeros)
def convertir_a_fecha(texto):
    return dt.datetime.strptime(texto,"%d/%m/%Y")
def curso_antes():
    nombre_curso=""
    fecha_antes=convertir_a_fecha(cursos[0]["fecha_fin"])
    for c in cursos:
        f=convertir_a_fecha(c["fecha_fin"])
        if f<fecha_antes:
            fecha_antes=f
            nombre_curso=c["denominacion"]
    
    print(f"El curso más antiguo es {nombre_curso}")
    
    
def curso_media_mayor():
    nombre_curso=""
    media_alta=media(cursos[0]["calificaciones"])
    for c in cursos:
        m=media(c["calificaciones"])
        if m>media_alta:
            #actualizamos variables.
            media_alta=m #la nueva media.
            nombre_curso=c["denominacion"]
    
    print(f"El curso con la media más alta es {nombre_curso}")

#Llamadas a las funciones (siempre hay que ponerlas abajo, no funciona como las variables.)
curso_antes()
curso_media_mayor() 
    
"""

import streamlit as st
import datetime as dt #si quiero usar DT tengo que ponerlo así: import datetime as dt. 
cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador certificado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"10/03/2025"},
]

def media(numeros):
    suma=0
    for n in numeros:
        suma+=n
    return suma/len(numeros)
def convertir_a_fecha(texto):
    return dt.datetime.strptime(texto,"%d/%m/%Y")
def curso_antes():
    nombre_curso=""
    fecha_antes=convertir_a_fecha(cursos[0]["fecha_fin"])
    for c in cursos:
        f=convertir_a_fecha(c["fecha_fin"])
        if f<fecha_antes:
            fecha_antes=f
            nombre_curso=c["denominacion"]
    
    print(f"El curso más antiguo es {nombre_curso}")
    
    
def curso_media_mayor():
    nombre_curso=""
    media_alta=media(cursos[0]["calificaciones"])
    for c in cursos:
        m=media(c["calificaciones"])
        if m>media_alta:
            #actualizamos variables.
            media_alta=m #la nueva media.
            nombre_curso=c["denominacion"]
    
    print(f"El curso con la media más alta es {nombre_curso}")

#Llamadas a las funciones (siempre hay que ponerlas abajo, no funciona como las variables.)
st.write(curso_antes())
st.write(curso_media_mayor())