import random as rd

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
