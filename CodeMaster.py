import random

digitos = ('0','1','2','3','4','5','6','7','8','9')

codigo = ''
for i in range(4):
    candidato = random.choice(digitos)
    
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

print('''
    
██████╗ ██████╗ ██████╗ ███████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██║  ██║█████╗      ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║     ██║   ██║██║  ██║██╔══╝      ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  
      
      ''')
print ("Bienvenido/a!")
print ("Tienes que adivinar un numero de 4 cifras distintas.")
propuesta = input("¿Que codigo propones?: ")

intentos = 1

while len(propuesta) <= 4:

    while propuesta != codigo:
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0

        for i in range(4):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos + 1
            elif propuesta[i] in codigo:
                coincidencias = coincidencias + 1
        print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
              "aciertos y ", coincidencias, "coincidencias.")
        print(codigo)
        propuesta = input("Propón otro codigo: ")
        if propuesta == codigo:
            print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
            if intentos < 3:
                print("eh... bro, COMO?????")
            if intentos == 3:
                print("A la tercera va la vencida!!!")
            if intentos == 5:
                print("Increible!! PD: Tranqui no hay rima jajaja")
            if intentos in range (5,19):
                print("Nada mal!")
            if intentos in range (20,50):
                print("Bien, has tardado un poco, pero lo conseguiste!")
            if intentos in range (50,100):
                print("Vaya, tienes paciencia lo reconozco!")
            if intentos in range > 100:
                print("Como has llegado tan lejos?!")
else:
    print("Error, tu codigo debe tener 4 digitos.")
<<<<<<< HEAD
    propuesta = input("Propón otro codigo: ")
    while propuesta != codigo:
        intentos = intentos + 1
        aciertos = 0
        coincidencias = 0

    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
            print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
                  "aciertos y ", coincidencias, "coincidencias.")
            print(codigo)
            if propuesta == codigo:
                print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
            if intentos < 3:
                print("eh... bro, COMO?????")
            if intentos == 3:
                print("A la tercera va la vencida!!!")
            if intentos == 5:
                print("Increible!! PD: Tranqui no hay rima jajaja")
            if intentos in range (5,19):
                print("Nada mal!")
            if intentos in range (20,50):
                print("Bien, has tardado un poco, pero lo conseguiste!")
            if intentos in range (50,100):
                print("Vaya, tienes paciencia lo reconozco!")
            if intentos in range > 100:
                print("Como has llegado tan lajos?!")
=======
    print("GAME OVER :(")
>>>>>>> 13f7316a8e0b0cfdd4557b67254102943617287e
