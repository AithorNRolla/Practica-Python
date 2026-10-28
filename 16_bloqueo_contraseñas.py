#Solicita la introducción de una contraseña, si es correcta
#le dice que es un usuario válido, si no, que se vuelva a pedir.
#Máximo tres intentos. Si el tercer intento acierta es válido, si no le dirá contraseña no válida. 


contraseña_buena = "1492" 
intentos = 0
ok = False  
#esto de aquí arriba de momento está bien construído. 
while intentos< 3 and not ok:
    intento_usuario = input(f"Introduce la contraseña (Intento {intentos+1} de 3): ")
    
    if intento_usuario == contraseña_buena: 
       ok = True 
    else:
     intentos += 1 
     if intentos < 3:
         print("Contraseña incorrecta, inténtelo de nuevo.\n")
            
if ok:
    print("\n Usuario válido, has ingresado corréctamente.")
else:
    print("\nUsuario incorrecto, hasta agotado tus intentos, inténtelo más tarde.")
    
    
#El ejercicio está bien hecho (aunque está sacado con IA), he aprendido que el while/else deben de ir a diferente altura,
#uno abre y el otro cierra. Aquí abajo quizás ponga la manera que haga el profesor o los compañeros. 