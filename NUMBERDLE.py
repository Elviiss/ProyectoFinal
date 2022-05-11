print('''
 .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____  _____  | || | _____  _____ | || | ____    ____ | || |   ______     | || |  _________   | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
| ||_   \|_   _| | || ||_   _||_   _|| || ||_   \  /   _|| || |  |_   _ \    | || | |_   ___  |  | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
| |  |   \ | |   | || |  | |    | |  | || |  |   \/   |  | || |    | |_) |   | || |   | |_  \_|  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
| |  | |\ \| |   | || |  | '    ' |  | || |  | |\  /| |  | || |    |  __'.   | || |   |  _|  _   | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
| | _| |_\   |_  | || |   \ `--' /   | || | _| |_\/_| |_ | || |   _| |__) |  | || |  _| |___/ |  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
| ||_____|\____| | || |    `.__.'    | || ||_____||_____|| || |  |_______/   | || | |_________|  | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''')                                                                                                                                                                                                                         

import random
def obtenerNumSecreto(digitosNum):
     numeros = list(range(10))
     random.shuffle(numeros)
     numSecreto = ''
     for i in range(digitosNum):
         numSecreto += str(numeros[i])
     return numSecreto

def obtenerPistas(conjetura, numSecreto):
     if conjetura == numSecreto:
         return '¡Lo has adivinado!'

     pista = []

     for i in range(len(conjetura)):
         if conjetura[i] == numSecreto[i]:
             pista.append('Fermi')
         elif conjetura[i] in numSecreto:
             pista.append('Pico')
     if len(pista) == 0:
         return 'Panecillos'

     pista.sort()
     return ' '.join(pista)

def esSoloDigitos(num):
     
     if num == '':
         return False

     for i in num:
         if i not in '0 1 2 3 4 5 6 7 8 9'.split():
             return False

     return True

def jugarDeNuevo():
     
     print('¿Deseas volver a jugar? (sí o no)')
     return input().lower().startswith('s')

digitosNum = 3
MAXADIVINANZAS = 10

print('Estoy pensando en un número de %s dígitos. Intenta adivinar cuál es.' % (digitosNum))
print('Aquí hay algunas pistas:')
print('Cuando digo:    Eso significa:')
print('  Pico          Un dígito es correcto pero en la posición incorrecta.')
print('  Fermi         Un dígito es correcto y en la posición correcta.')
print('  Panecillos    Ningún dígito es correcto.')

while True:
     numSecreto = obtenerNumSecreto(digitosNum)
     print('He pensado un número. Tienes %s intentos para adivinarlo.' % (MAXADIVINANZAS))

     numIntentos = 1
     while numIntentos <= MAXADIVINANZAS:
         conjetura = ''
         while len(conjetura) != digitosNum or not esSoloDigitos(conjetura):
             print('Conjetura #%s: ' % (numIntentos))
             conjetura = input()

         pista = obtenerPistas(conjetura, numSecreto)
         print(pista)
         numIntentos += 1

         if conjetura == numSecreto:
             break
         if numIntentos > MAXADIVINANZAS:
             print('Te has quedado sin intentos. La respuesta era %s.' % (numSecreto))

     if not jugarDeNuevo():
         break