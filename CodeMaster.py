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
print ("Tienes que adivinar un numero de", 4, "cifras distintas.")
propuesta = input("¿Que codigo propones?: ")


intentos = 1
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

    propuesta = input("Propón otro codigo: ")

print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")

if intentos < 3:
    print("eh... bro, COMO?????")
if intentos == 3:
    print("A la tercera va la vencida!!!")
if intentos <= 5:
    print("Increible!! PD: Tranqui no hay rima jajaja")
if intentos <= 10:
    print("Nada mal!")
if intentos <= 25:
    print("Bueno te a costado un poco, pero bien hecho!")
if intentos <= 50:
    print("LOL, como has llegado hasta aquí??")
if intentos <= 80:
    print("Tienes paciencia, lo admito")
if intentos <= 100:
    print("Eh... tas bien??")
if intentos <= 150:
    print("Vaya... sigues aquí??")
