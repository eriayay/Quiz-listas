#clase Persona
class Persona:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
        

#clase Habitacion
class Habitacion:
    def __init__(self, numeroHab):
        self.numeroHab = numeroHab
        self.huesped = None
        self.siguiente = None
        

# Clase para guardar la informacion de las entradas
class EntradaPersona:
    def __init__(self, persona, numeroHab):
        self.persona = persona
        self.numeroHab = numeroHab
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
    def registrar(self, numeroHab):
        nueva_habitacion = Habitacion(numeroHab)
        
        if self.cabeza == None:
            self.cabeza = nueva_habitacion
        else:
            habitacion_actual = self.cabeza
            while(habitacion_actual.siguiente):
                habitacion_actual = habitacion_actual.siguiente
                
            habitacion_actual.siguiente = nueva_habitacion
            
    #Buscar habitacion por numeroHab
    def buscar(self, numeroHab):
        habitacion_actual = self.cabeza
        while(habitacion_actual):
            if habitacion_actual.numeroHab == numeroHab:
                break
            habitacion_actual = habitacion_actual.siguiente

        if habitacion_actual != None:
            return habitacion_actual
        else:
            return habitacion_actual

    #Asignar habitacion
    def asignar(self, numeroHab, persona):
        habitacion_actual = buscar(numeroHab)
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
                print(habitacion_actual.numeroHab)
            habitacion_actual = habitacion_actual.siguiente
        
    #Imprimir habitaciones disponibles
    def imprimirDisponibles(self):
        print("\nLas habitaciones disponibles son:")
        habitacion_actual = self.cabeza
        while(habitacion_actual):
            if habitacion_actual.huesped != None:
                print(habitacion_actual.numeroHab)
            habitacion_actual = habitacion_actual.siguiente


#clase lista libro de entradas
class Entradas:
    def __init__(self, listaPersonas, listaHabitaciones):
        self.cabeza = None
        self.listaPersonas = listaPersonas
        self.listaHabitaciones = listaHabitaciones

    #Agregar personas a la lista
    def agregar(self, cedula, numeroHab):
        persona = self.listaPersonas.buscar(cedula)
        if persona:
            nueva_entrada = EntradaPersona(persona, numeroHab)

            if self.cabeza is None:
                self.cabeza = nueva_entrada
            else:
                entrada_actual = self.cabeza
                while (entrada_actual.siguiente):
                    entrada_actual = entrada_actual.siguiente
                entrada_actual.siguiente = nueva_entrada
                # Tambien asigna la habitacion a la persona en la lista de habitaciones
                self.listaHabitaciones.asignar(numeroHab, persona)
            print("Asignacion correctamente realizada")
        else:
            print("Persona no registrada, por favor registrar primero")

    #Imprimir lista de entradas
    def imprimirEntradas(self):
        print("\nLibro de entradas:")
        entrada_actual = self.cabeza
        while entrada_actual:
            print("Cedula: " + str(entrada_actual.persona.cedula) + " Nombre: " + str(entrada_actual.persona.nombre) + " Habitacion: " + str(entrada_actual.numero_habitacion))
            entrada_actual = entrada_actual.siguiente

    #Imprimir entrada individual
    def imprimirIndividual(self, cedula):
        persona = self.listaPersonas.buscar(cedula)
        entrada_actual = self.cabeza
                while (entrada_actual):
                    if entrada_actual.persona == persona:
                        break
                    entrada_actual = entrada_actual.siguiente

                if entrada_actual.persona == persona:    
                    print("\nPersona actualmente en el hotel")
                    print("Cedula: " + str(entrada_actual.persona.cedula) + " Nombre: " + str(entrada_actual.persona.nombre) + " Habitacion: " + str(entrada_actual.numero_habitacion))
                else:
                    print("\nPersona no reside actualmente en el hotel")       