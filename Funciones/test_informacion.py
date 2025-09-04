import informacion

for i in range(13):
    nombres = input("Ingrese el nombre y apellido del paciente: ")
    informacion.agregar_nombre(nombres)
    anio = int(input("Ingrese el año de nacimiento del paciente: "))
    informacion.agregar_edad(anio)

informacion.mostrar_nombres()
informacion.mostrar_edades()
informacion.mostrar_mayor()
