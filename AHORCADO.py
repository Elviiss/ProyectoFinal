print('''

                            ███████╗██╗          █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗ 
██╔════╝██║         ██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
█████╗  ██║         ███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║
██╔══╝  ██║         ██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║
███████╗███████╗    ██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝
╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ 
                                                                                      



                                                                                                ''')

import random
IMAGENES_AHORCADO = ['''

   +---+
 |    |
      |
       |
       |
       |
   =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
   =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
   =========''', '''
 
   +---+
   |   |
   O   |
 _/|   |
       |
       |
   =========''', '''
 
   +---+
   |   |
   O   |
 _/|\_ |
       |
       |
   =========''', '''
 
   +---+
   |   |
   O   |
 _/|\_ |
 _/    |
       |
   =========''', '''

   +---+
   |   |
   O   |
 _/|\_ |
 _/ \_ |
       |
   =========''']

palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()
 
def obtenerPalabraAlAzar(listaDePalabras):
      
      índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
      return listaDePalabras[índiceDePalabras]
 
def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
      print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
      print()
 
      print('Letras incorrectas:', end=' ')
      for letra in letrasIncorrectas:
          print(letra, end=' ')
      print()
 
      espaciosVacíos = '_' * len(palabraSecreta)
 
      for i in range(len(palabraSecreta)): 
          if palabraSecreta[i] in letrasCorrectas:
              espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]
 
      for letra in espaciosVacíos: 
          print(letra, end=' ')
      print()
 
def obtenerIntento(letrasProbadas):
      
      while True:
          print('Adivina una letra:')
          intento = input()
          intento = intento.lower()
          if len(intento) != 1:
              print('Por favor, introduce una letra:')
          elif intento in letrasProbadas:
              print('Ya has probado esa letra, elige otra:')
          elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
              print('Por favor introduce una letra:')
          else:
              return intento

def jugarDeNuevo():
     
     print('¿Quieres jugar de nuevo?: (sí o no)')
     return input().lower().startswith('s')


letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
     mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

     
     intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

     if intento in palabraSecreta:
         letrasCorrectas = letrasCorrectas + intento

         
         encontradoTodasLasLetras = True
         for i in range(len(palabraSecreta)):
             if palabraSecreta[i] not in letrasCorrectas:
                 encontradoTodasLasLetras = False
                 break
         if encontradoTodasLasLetras:
             print('¡Sí! ¡La palabra secreta es: "' + palabraSecreta + '"¡Has ganado!')
             juegoTerminado = True
     else:
         letrasIncorrectas = letrasIncorrectas + intento

         
         if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
             mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
             print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
             juegoTerminado = True

     
     if juegoTerminado:
         if jugarDeNuevo():
             letrasIncorrectas = ''
             letrasCorrectas = ''
             juegoTerminado = False
             palabraSecreta = obtenerPalabraAlAzar(palabras)
         else:
             break
