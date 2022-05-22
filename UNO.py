import random as rd
##from playsound import playsound
##playsound('casinoluigi.wav')


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
         textoCarta+= pintar_Carta(carta)
      else:
         textoCarta+=pintar_Carta(carta)
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

def robar(jugador,numero,baraja):
   for p in range(numero):
      if len(baraja)>0:
         jugador["mano"].append(baraja[0])
         baraja=baraja[1:]
   return baraja

def pillarCartaRobo(jugador,cartaMesa,baraja):
   if cartaMesa["valor"]=="+4":
      print("\t*****ROBA 4 Cartas*****")
      baraja=robar(jugador,4,baraja)
      cartaMesa["robar"]=0
   elif cartaMesa["valor"]=="+2" and cartaMesa["robar"]>0:
      tengo=False
      for carta in jugador["mano"]:
         tengo=tengo or carta["valor"]=="+2"
      if not tengo:
         print("\t*****ROBA "+str(cartaMesa["robar"])+" Cartas*****")
         baraja=robar(jugador, cartaMesa["robar"],baraja)
         cartaMesa["robar"]=0
   return baraja

def coger_Carta(jugador, cartaEnMesa, baraja):
   repetir=True
   selecioniada=None
   while repetir:
      mostrar_Mano(jugador, True, cartaEnMesa)
      print("\nCarta en la mesa: ", pintar_Carta(monton[-1]))
      idCartaEscogida=input("Que carta quieres tirar (R para robar, S para salir, Cartas en la Baraja: "+str(len(baraja))+"):").capitalize()
      if idCartaEscogida=="R":
         if len(baraja)>0:
            baraja=robar(jugador,1,baraja)
         else:
            print("NO HAY CARTAS PARA ROBAR")
      elif idCartaEscogida=="S":
         
         print('''
                        \t\t██╗  ██╗ █████╗ ███████╗████████╗ █████╗     ██╗     ██╗   ██╗███████╗ ██████╗  ██████╗ 
                        \t\t██║  ██║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗    ██║     ██║   ██║██╔════╝██╔════╝ ██╔═══██╗
                        \t\t███████║███████║███████╗   ██║   ███████║    ██║     ██║   ██║█████╗  ██║  ███╗██║   ██║
                        \t\t██╔══██║██╔══██║╚════██║   ██║   ██╔══██║    ██║     ██║   ██║██╔══╝  ██║   ██║██║   ██║
                        \t\t██║  ██║██║  ██║███████║   ██║   ██║  ██║    ███████╗╚██████╔╝███████╗╚██████╔╝╚██████╔╝
                        \t\t╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ 
                                                                                        ''')
         return -1,baraja
      elif idCartaEscogida.isnumeric() and int(idCartaEscogida)>0 and int(idCartaEscogida)<=len(jugador["mano"]):
         cartaEscogida=jugador["mano"][int(idCartaEscogida)-1]
         if seguir_Reglas(cartaEscogida,cartaEnMesa):
            jugador["mano"]=jugador["mano"][0:int(idCartaEscogida)-1]+jugador["mano"][int(idCartaEscogida):]
            if(cartaEscogida["color"]=="NEGRO"):
               cartaEscogida["color"]=escoger_Color()
            repetir=False
         else:
            print("ESA CARTA NO VALE")
   return cartaEscogida,baraja

def puntos(carta):
   if carta["valor"]=="+4":
      return 100
   if carta["valor"]=="+2":
      return 20
   if carta["valor"]=="COMODIN":
      return 20
   if carta["valor"]=="SALTO":
      return 50
   if carta["valor"]=="CAMBIO":
      return 50
   return int(carta["valor"])

def jugar_Carta(jugador, cartaEnMesa, baraja):
   repetir=True
   selecioniada=None
   while repetir:
      print("Tiene "+str(len(jugador["mano"]))+" cartas")
      
      cartasValidas=[]
      cartasColor={}
      for i,carta in enumerate(jugador["mano"]):
         if seguir_Reglas(carta,cartaEnMesa):
            cartasValidas.append(i)
         if carta["color"]!="NEGRO":
            if carta["color"] in cartasColor:
               cartasColor[carta["color"]]+=1
            else:
               cartasColor[carta["color"]]=1
      idCartaSeleccionada=-1
      if len(cartasValidas)==0:
         if len(baraja)>0:
            print("\tRobo carta")
            baraja=robar(jugador,1,baraja)
         else:
            print("NO HAY CARTAS PARA ROBAR")
            return None,baraja
      else:
         for idCarta in cartasValidas:
            if idCartaSeleccionada<0:
               idCartaSeleccionada=idCarta
            else:
               if not jugador["mano"][idCarta]["valor"].isnumeric():
                  idCartaSeleccionada=idCarta
      
         if jugador["mano"][idCartaSeleccionada]["color"]=="NEGRO":
            color=""
            colorNumero=0
            for c in cartasColor:
               if cartasColor[c]>colorNumero:
                  colorNumero=cartasColor[c]
                  color=c
            jugador["mano"][idCartaSeleccionada]["color"]=c
         repetir=False
   cartaEscogida=jugador["mano"][idCartaSeleccionada]
   jugador["mano"]=jugador["mano"][0:int(idCartaSeleccionada)]+jugador["mano"][int(idCartaSeleccionada)+1:]
   return cartaEscogida,baraja

colores=["NEGRO", "AZUL", "VERDE", "ROJA", "AMARILLA"]
baraja=[] 
monton=[] 
baraja=crearBaraja()

jugadores=[{"nombre":"","mano":[], "tipo":"perdedor", "puntuacion":0},
   {"nombre":"Elvis","mano":[], "tipo": "bot", "puntuacion":0},
   {"nombre":"Navarro","mano":[], "tipo": "bot", "puntuacion":0},
   {"nombre":"Jaime","mano":[], "tipo": "bot", "puntuacion":0}]
jugadores[0]["nombre"]=input("Dime tu nombre: ")

for p in range(7):
   for jugador in jugadores:
      jugador["mano"].append(baraja[0])
      baraja=baraja[1:]

monton.append(baraja[0])
baraja=baraja[1:]
if(monton[0]["color"]=="NEGRO"):
   monton[0]["color"]=rd.choice(colores[1:])

continuar=True
idJugador=0
direccionJuego=+1
numeroJugadores=len(jugadores)
while continuar:
   if len(baraja)<=0:
        continuar=False
   if monton[-1]["valor"]=="SALTO":
        idJugador+=direccionJuego   
        idJugador=(numeroJugadores+idJugador) if idJugador<0 else idJugador % numeroJugadores
   jugador=jugadores[idJugador]
   print("\nTurno de " + jugador["nombre"]+" - "+str(jugador["puntuacion"])+ " puntos")
   baraja=pillarCartaRobo(jugador,monton[-1],baraja)

   if jugador["tipo"]=="bot":
        cartaEscogida,baraja=jugar_Carta(jugador,monton[-1],baraja)
        print("\tTira "+pintar_Carta(cartaEscogida))
   else:
      cartaEscogida,baraja=coger_Carta(jugador,monton[-1],baraja)
   if (cartaEscogida==-1):
      continuar=False
   else:
      if cartaEscogida!=None:
         jugador["puntuacion"]+=puntos(cartaEscogida)
         cartaEscogida["robar"]+=monton[-1]["robar"]
         monton.append(cartaEscogida)
      print("Tine puntuación "+str(jugador["puntuacion"]))
      if len(jugador["mano"])==0 or jugador["puntuacion"]>=300:
         continuar=False
         print('''
                        \t\t███████ ███████ ██      ██  ██████ ██ ██████   █████  ██████  ███████ ███████ ██ ██ ██ 
                        \t\t██      ██      ██      ██ ██      ██ ██   ██ ██   ██ ██   ██ ██      ██      ██ ██ ██ 
                        \t\t█████   █████   ██      ██ ██      ██ ██   ██ ███████ ██   ██ █████   ███████ ██ ██ ██ 
                        \t\t██      ██      ██      ██ ██      ██ ██   ██ ██   ██ ██   ██ ██           ██          
                        \t\t██      ███████ ███████ ██  ██████ ██ ██████  ██   ██ ██████  ███████ ███████ ██ ██ ██ ''')
         print (jugador["nombre"]+ "  GANA LA PARTIDA"+((" Con puntuación de "+str(jugador["puntuacion"])) if (jugador["puntuacion"]>=300) else " SE ha quedado sin cartas"))
      if monton[-1]["valor"]=="CAMBIO":
         direccionJuego*=-1
      idJugador+=direccionJuego
      idJugador=(numeroJugadores+idJugador) if idJugador<0 else idJugador % numeroJugadores
