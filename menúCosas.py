def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    print('''
     ██╗ ██╗   ██╗███████╗ ██████╗  ██████╗ ███████╗
     ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗██╔════╝
     ██║██║   ██║█████╗  ██║  ███╗██║   ██║███████╗
██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║╚════██║
╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝███████║
 ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝
          ''')
    print ("1. Ahorcado")
    print ("2. Uno de carreras")
    print ("3. Modo locura")
    print ("4. Code Master")
    print ("5. Numberdle")
    print ("6. Salir")
     
    print ("\nElige una opcion.")
 
    opcion = Menu()
 
    if opcion == 1:
        print ("Ahorcado")
        # Acceso directo al archivo
        
    elif opcion == 2:
        print ("Uno de carreras")
        # Acceso directo al archivo

    elif opcion == 3:
        print("Modo locura")
        # Acceso directo al archivo
        
    elif opcion == 4:
        print("Code Master")
        # Acceso directo al archivo
        
    elif opcion == 5:
        print("Numberdle")
        # Acceso directo al archivo
        
    elif opcion == 6:
        salir = True
    else:
        print ("Error, introduce un numero comprendido entre 1 y 6")
 
print ("Hasta luego ciruelo!")