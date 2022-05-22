# import os
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
     ██╗██╗   ██╗███████╗ ██████╗  ██████╗ ███████╗
     ██║██║   ██║██╔════╝██╔════╝ ██╔═══██╗██╔════╝
     ██║██║   ██║█████╗  ██║  ███╗██║   ██║███████╗
██   ██║██║   ██║██╔══╝  ██║   ██║██║   ██║╚════██║
╚█████╔╝╚██████╔╝███████╗╚██████╔╝╚██████╔╝███████║
 ╚════╝  ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝
          ''')
    print ("1. Ahorcado")
    print ("2. Uno")
    print ("3. Snake")
    print ("4. Code Master")
    print ("5. Numberdle")
    print ("6. Pong")
    print ("6. Salir")
     
    print ("\nElige una opcion.")
 
    opcion = Menu()
 
    if opcion == 1:
        print ("Has elegido Ahorcado")
        import AHORCADO
        
    elif opcion == 2:
        print ("Has elegido el Uno ")
        import UNO

    elif opcion == 3:
        print("Has elegido Snake")
        import snake
        
    elif opcion == 4:
        print("Has elegido Code Master")
        import CodeMaster
        
    elif opcion == 5:
        print("Has elegido Numberdle")
        import NUMBERDLE
        
    elif opcion == 6:
        print("Has elegido el Pong")
        import pong
        
    elif opcion == 7:
        salir = True
    else:
        print ("Error, introduce un numero comprendido entre 1 y 6")
 
print ("Hasta luego ciruelo!")
