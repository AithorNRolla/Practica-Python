contraseña_buena = "1492" 
intentos = 0
ok=False
#esto de aquí arriba de momento está bien construído. 
while intentos< 3 and not ok:
    intento_usuario = input(f"Introduce la contraseña (Intento {intentos+1} de 3): ")
    
    if intento_usuario == contraseña_buena: 
       print("\n Usuario válido, has ingresado corréctamente.")
       ok=True
       break
    else:
        print("Vuelve a intentarlo")
            
if not ok:
   print("Vuelve a intentarlo")
   