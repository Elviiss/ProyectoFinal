class Personaje:
      def __init__(self):
        self.nombre = ""
        self.salud = 1
        self.salud_max = 1
    
class Jugador(Personaje):
      def __init__(self):
        Personaje.__init__(self)
        self.estado = 'normal'
        self.salud = 10
        self.salud_max = 10


p = Jugador()
p.nombre = input("Cual es el nombre del personaje? ")
print ("(Escribe ayuda para obtener una lista de acciones)n")
print ("%s bienvenido a Tame, preparate para esta locura...") % p.nombre
