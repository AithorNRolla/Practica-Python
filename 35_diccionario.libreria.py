"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
""" 

#Primero vamos a crear la variable tocha: esto nos permitirá almacenar la información. 
librería=[]
#El jodido bucle y las opciones: 
while True:
    print("1 - Nuevo libro")
    print("2 - Mostrar todo")
    print("3 - Búsqueda por título")
    print("4 - Libros por precio máximo")
    print("5 - Salir")
    opcion=input("Selecciona una opción 1/5:  ").strip() #El strip borra espacios en los textos.
    #Cerramos bucle.
    if opcion=="5":
        print("Gracias por su visita!")
        break  #Aquí rompemos el bucle y empiezan las opciones de la 1 a la 5. 
    elif opcion=="1":
        print("Añadir nuevo libro")
        titulo_nuevo=input("Introduce el título nuevo:  ").strip() #El strip borra espacios en los textos.
        ya_existe=False #esto me deniega si el título ya está.
        for libro in librería:
            if libro ["titulo"].lower()==titulo_nuevo.lower(): #lower hace que todo esté en minúsculas. 
                ya_existe=True #Esto me permite introducir el nuevo título. 
        if ya_existe==False:
            autor=input("Introduce el autor:  ").strip() #El strip borra espacios en los textos.
            precio=float(input("Introduce el precio:  "))
            tarjeta_libro={
                "titulo":titulo_nuevo,
                "autor": autor,
                "precio": precio
            }
            librería.append(tarjeta_libro) #aquí añadimos cualquier cosa al final de la lista. 
            print("¡Libro guardado con éxito!")
        else: 
         print("Este libro ya está en la librería.")
            
    #Seguramente tengamos que poner algo aquí fijo. 
    elif opcion=="2":
        print("[Listado de todos los libros]")
        for c in librería:
            print(c["titulo"])
    #Fijo que nos comemos mierdón aquí por bucle. 
    elif opcion=="3":
        print("Búsqueda por título:  ")
        busqueda=input()
        encontrado=False
        for c in librería:  #Aquí es dónde pedimos más información del libro.
            if c["titulo"].lower()==busqueda.lower():  #lower hace que todo esté en minúsculas. 
                print("¡Encontrado!")
                print(f"Título: {c['titulo']}") #la F roja de formato me permite enviarle eso al usuaio. 
                print(f"Autor: {c['autor']}")
                print(f"Precio: {c['precio']}")
                encontrado=True
        if encontrado==False:
            print("No se ha encontrado el libro.")       
    #Dejamos espacio entre opciones para anotar.  
    elif opcion=="4":
        print("Precios máximos:  ")
        precio_maximo=float(input("Introduce máximos:  "))
        print(f"Libros que cuestan {precio_maximo}€ o menos:  ")
        encontrado=False
        for c in librería:
            if c["precio"]<=precio_maximo:
                print(f"{c['titulo']} ({c['precio']}€)")
                encontrado=True
            if encontrado==False: #Al loro por que me daba error por estár pegado a la izquierda. 
             print("No hay ningún libro con ese precio. ")
    #La judeada histórica, aquí te clavan. 
    else:
        print("Opción no válida, elija entre 1/5.")
        
#Hasta aquí el ejercicio ha sido escrito por mí en su totalidad. 

"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o inferior al introducido
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa

libros=[]
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Nuevo libro")
    print("2 - Mostrar todos")
    print("3 - Buscar por título")
    print("4 - Libros por precio máximo")
    print("5 - Salir")
def titulos():
    print("Títulos de los libros:")
    for lib in libros:
        print(f"Título: {lib["titulo"]} precio:{lib["precio"]}")
def buscar_titulo(titulo):   
    encontrado=False    
    for i in libros:
        if titulo.lower() == i["titulo"].lower():
            print("Se ha encontrado tu libro")
            print(f"Título: {i['titulo']} Autor: {i['autor']} Precio: {i['precio']}")
            encontrado= True
            break
    if not encontrado:
        print("Libro no encontrado")
    return encontrado
def nuevo_libro():
	titulo = input("Título: ")
	autor = input("Autor: ")
	try:
		precio = float(input("Precio: "))
	except ValueError:
		print("Precio no válido. No se agregó el libro.")
		return
	if not buscar_titulo(titulo):
		libros.append({"titulo": titulo, "autor": autor, "precio": precio})
		print("Libro agregado.")
	else:
		print("Libro repetido, no se agregó")
def libros_por_precio_maximo(max_precio):  
    titulos = [n["titulo"] for n in libros if n["precio"]<=max_precio]    
    if len(titulos)>0:
        print(f"Libros con precio <= {max_precio}:")
        for j in titulos:
            print(j)  
    else:
        print("No hay libros con ese precio o inferior.")
opcion="0"    
while opcion!="5":
	mostrar_menu()
	opcion=input("Elige una opción: ")
	if opcion == "1":
		nuevo_libro()
	elif opcion == "2":
		titulos()
	elif opcion == "3":
		buscar=input("Introduce el titulo del libro que quieres buscar: ")
		buscar_titulo(buscar)
	elif opcion == "4":
		try:
			max_precio = float(input("Precio máximo: "))
			libros_por_precio_maximo(max_precio)
		except ValueError:
			print("Precio no válido.")
	elif opcion == "5":
		print("Saliendo del programa...")
	else:
		print("Opción no válida. Intenta de nuevo.") 
  """
  
  #Esto es del profesor. 