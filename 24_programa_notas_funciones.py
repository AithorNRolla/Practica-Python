#Al iniciar el programa se debe mostrar el siguiente menú:
#1 - Añadir nota.
#2 - Mostrar notas extremas. 
#3 - Total de aprobados. 
#4 - Nota media. 
#5 - Mostrar todas.
#6 - Salir. 

#El usuario elige una opción (1 al 6) y el programa le muestra
#los datos necesarios para llevar a cabo la acción. Después, vuelve a salir el menú. 
#Así hasta que elija la opción de salir. 

notas=[]
#funciones propias
def menu():
    print("\n Menú de notas")
    print("1: Añadir nota")
    print("2: Mostrar nota extremas")
    print("3: Total de aprobados")
    print("4: Nota media")
    print("5: Mostrar todas")
    print("6: Salir")
def aprobados():
    if len(notas)==0:
                print("Todavía no hay aprobados")
            else:
                total_aprobados=0
                for num in notas:
                    if num >5:
                        total_aprobados=total_aprobados+1         
             
    

#programa principal
opcion=0
aprobados=0
media=0
todo=0

while opcion!=6: #Recordemos que la ! signifira "diferente de". 
    menu()
    opcion=int(input("Elija una opción del 1 al 6   "))
    if opcion==1:
        nueva_nota=float(input("Añadir nota: "))
        notas.append(nueva_nota)
        print("Nota guardada ")
    elif opcion==2:
        if len(notas)==0:
            print("Todavía no hay notas extremas")
        else:
            nota_extrema=max(notas)
            nota_minima=min(notas)
            print(f"Notas extremas {nota_extrema}")
            print(f"Notas mínimas {nota_minima}")
    elif opcion==3:
            print(f"Total de aprobados: {total_aprobados}")
    elif opcion==4:
        if len(notas)==0:
            print("Todavía no hay notas medias")
        else:
            media=sum(notas)/len(notas)
            print(f"La nota media es {media}")
    elif opcion==5:
        if len(notas) ==0:
            print("Todavía no hay notas")
        else:
         print(f"Mostrar todas {notas} ")
    elif opcion==6:
        print("Salir")
        
#Personalmente todo el programa ha sido casi en su totalidad, ayuda de la IA. He aprendido que hay qu ser cuidadoso,
#cada apartado de if y else necesitan de más comandos que digan que hay que hacer. Además de las variables al principio. 
#Hoy 29/19/2026 he construído esto, vamos poco a poco. 