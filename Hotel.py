#clase Persona
class Persona:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
        

#clase Habitacion
class Habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.huesped = None
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
            
    #Buscar personas por cedula
    def buscar(self, cedula):
        persona_actual = self.cabeza
        while(persona_actual):
            if persona_actual.cedula == cedula:
                break
            persona_actual = persona_actual.siguiente

        if persona_actual != None:
            return persona_actual
        else:
            print("Persona no registrada")
            return persona_actual
        
        
#Clase lista de habitaciones
class ListaHabitaciones:
    def __init__(self):
        self.cabeza = None
        
    #Registrar habitaciones
    def registrar(self, numero):
        nueva_habitacion = Habitacion(numero)
        
        if self.cabeza == None:
            self.cabeza = nueva_habitacion
        else:
            habitacion_actual = self.cabeza
            while(habitacion_actual.siguiente):
                habitacion_actual = habitacion_actual.siguiente
                
            habitacion_actual.siguiente = nueva_habitacion
            
    #Buscar habitacion por numero
    def buscar(self, numero):
        habitacion_actual = self.cabeza
        while(habitacion_actual):
            if habitacion_actual.numero == numero:
                break
            habitacion_actual = habitacion_actual.siguiente

        if habitacion_actual != None:
            return habitacion_actual
        else:
            return habitacion_actual

    #Asignar habitacion
    def asignar(self, numero, persona):
        habitacion_actual = buscar(numero)
        if habitacion_actual != None:
            habitacion_actual.huesped = persona
        else:
            print("habitacion no registrada")

    #Imprimir habitaciones ocupadas
    def imprimirOcupadas(self):
        print("\nLas habitaciones ocupadas son:")
        habitacion_actual = self.cabeza
        while(habitacion_actual):
            if habitacion_actual.huesped == None:
                print(habitacion_actual.numero)
            habitacion_actual = habitacion_actual.siguiente
        
    #Imprimir habitaciones disponibles
    def imprimirDisponibles(self):
        print("\nLas habitaciones disponibles son:")
        habitacion_actual = self.cabeza
        while(habitacion_actual):
            if habitacion_actual.huesped != None:
                print(habitacion_actual.numero)
            habitacion_actual = habitacion_actual.siguiente


#clase lista libro de entradas
class Entrada:
    def __init__(self):
        self.cabeza = None

    #Agregar personas a la lista
    def agregar(self):