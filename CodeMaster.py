import random

digitos = ('0','1','2','3','4','5','6','7','8','9')

codigo = ''
for i in range(4):
    candidato = random.choice(digitos)
    
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

print('''
    
██████╗ ██████╗ ██████╗ ███████╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██║  ██║█████╗      ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║     ██║   ██║██║  ██║██╔══╝      ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  
      
      ''')
print ("Bienvenido/a!")
print ("Tienes que adivinar un código secreto de 4 cifras distintas.")
propuesta = input("¿Que codigo propones?: ")

intentos = 1

while True:

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
              "aciertos y ", coincidencias, "coincidencias.\n")
#        print('Comprobar salidas if:', codigo)
        propuesta = input("Propón otro codigo: ")
        if len(propuesta) > 4:
            print("Introduce no más de 4 digitos.")
        if propuesta == codigo:
            print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
            if intentos < 3:
                print("eh... bro, COMO?????")
            if intentos == 3:
                print("A la tercera va la vencida!!!")
            if intentos == 5:
                print("Increible!! PD: Tranqui no hay rima jajaja")
            if intentos in range (6,19):
                print("Nada mal!")
            if intentos in range (20,50):
                print("Bien, has tardado un poco, pero lo conseguiste!")
            if intentos in range (50,100):
                print("Vaya, tienes paciencia lo reconozco!")
            if intentos > 100:
                print("Como has llegado tan lejos?!")
else:
    print("Error, tu codigo debe tener 4 digitos.")
