#clase Persona
class Persona:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
        
#clase Habitacion
class Habitacion:
    def __init__(self, numero, huesped):
        self.numero = numero
        self.huesped = huesped
        self.siguiente = None
        
#Clase lista de personas
class ListaPersonas:
    def __init__(self):
        self.cabeza = None
        
    #Registrar personas
    def registrar(self, cedula, nombre):
        nueva_persona = Persona(cedula, nombre)
        
        if self.cabeza == None:
            self.cabeza = nueva_persona
        else:
            persona_actual = self.cabeza
            while(persona_actual.siguiente):
                persona_actual = persona_actual.siguiente
                
            persona_actual.siguiente = nueva_persona
            
    def buscar(self, cedula):
        
        
        
#clase lista enlazada entradas
class Entrada:
    def __init__(self):
        self.cabeza = None

    #Agregar personas a la lista
    def agregar(self, persona):