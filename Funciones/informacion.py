nombre_paciente = []
edad = []

def agregar_nombre(nombre):
    nombre_paciente.append(nombre)
    print(f"El nombre se ha agregado correctamente.")

def agregar_edad(anio_paciente):
    edad.append(2025 - anio_paciente)
    print(f"La edad se ha agregado correctamente. \n {2025 - anio_paciente}")

def mostrar_nombres():
    print(f"Los nombres de los pacientes son: {nombre_paciente}")

def mostrar_edades():
    print(f"Las edades de los pacientes son: {edad}")

def mostrar_mayor():
    mayor = max(edad)
    mayor_i = edad.index(mayor)
    print(f"{nombre_paciente[mayor_i]} con la edad de {mayor} años es mayor a los demas pacientes")

