import random as rd

print('''
         \t\t██╗   ██╗███╗   ██╗ ██████╗ 
         \t\t██║   ██║████╗  ██║██╔═══██╗
         \t\t██║   ██║██╔██╗ ██║██║   ██║
         \t\t██║   ██║██║╚██╗██║██║   ██║
         \t\t╚██████╔╝██║ ╚████║╚██████╔╝''')

def crearBaraja():
   baraja=[]
   for v in range(0,9):
      for color in colores[1:]:
         for p in range(2 if v>0 else 1):
            baraja.append({"color":color,"valor":str(v), "robar":0})
   for p in range(4):
      baraja.append({"color":"NEGRO", "valor":"+4", "robar":4})
      baraja.append({"color":"NEGRO", "valor":"COMODIN", "robar":0})
   for p in range(3): 
      for color in colores[1:]:
         baraja.append({"color":color, "valor":"+2", "robar":2})
         baraja.append({"color":color, "valor":"CAMBIO", "robar":0})
         baraja.append({"color":color, "valor":"SALTO", "robar":0})
   rd.shuffle(baraja)
   return baraja

def seguir_Reglas(cartaEscogida,cartaEnMesa):
   if cartaEscogida["color"]=="NEGRO":
      return True
   else:
      return cartaEnMesa["color"]==cartaEscogida["color"] or cartaEnMesa["valor"]==cartaEscogida["valor"]
def pintar_Carta(carta):
   return ((carta["color"]+" ") if carta["color"]!="NEGRO" else "") +carta["valor"] + ("("+str(carta["robar"])+")" if carta["robar"]>0 else "")

def mostrar_Mano(jugador, numeradas = False, cartaMesa = None):
   i = 1
   col = 0
   cadenaSalida = ""
   for carta in jugador["mano"]:
      
      textoCarta=((str(i)+" " if numeradas else ""))
      if cartaMesa!=None and seguir_Reglas(carta,cartaMesa):
         textoCarta+= pintarCarta(carta)
      else:
         textoCarta+=pintarCarta(carta)
      cadenaSalida+=("\t" if col>0 else "\n")+textoCarta
      if(col==3):
         col=0
      else:
         col+=1
      i+=1
   print(cadenaSalida)
         
def escoger_Color():
   colorElegido=""
   repetir=True
   while repetir:
      i=1
      for color in colores[1:]:
         print(str(i)+" "+color)
         i+=1
      colorElegido=input("Escoge color: ")
      if colorElegido.isnumeric() and int(colorElegido)>0 and int(colorElegido) <= len(colores)-1:
         repetir=False
   return colores[int(colorElegido)]

def robar():
   pass

def coger_Carta():
   pass

def jugar_Carta():
   pass

def puntos():
   pass

colores=["NEGRO", "AZUL", "VERDE", "ROJA", "AMARILLA"]
baraja=[] 
monton=[] 
baraja=crearBaraja()   
