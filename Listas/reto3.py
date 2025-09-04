platos = ["Pizza", "Hamburguesa", "Cevichochos"]
print(platos)
opciones = int(input("Ingrese la opcion que desea \n1.-Añadir plato al menu" \
"\n2.-Buscar en el menu \n3.-Eliminar plato del menu\n4.-Mostrar platos del menu \n"))

if opciones == 1:
    nuevo_plato = input("Ingrese el nombre del nuevo plato: ")
    platos.append(nuevo_plato)
    print(f"Plato añadido: {nuevo_plato}")
    print("Platos en el menu:")
    for plato in platos:
        print(f" - {plato}")

elif opciones == 2:
    buscar_plato = input("Ingrese el nombre del plato que desea buscar: ")
    if buscar_plato in platos:
        print(f"Plato encontrado: {buscar_plato}")
    else:
        print(f"Plato no encontrado: {buscar_plato}")

elif opciones == 3:
    eliminar_plato = input("Ingrese el nombre del plato que desea eliminar: ")
    if eliminar_plato in platos:
        platos.remove(eliminar_plato)
        print(f"Plato eliminado: {eliminar_plato}")
        print("Platos en el menu:")
        for plato in platos:
            print(f" - {plato}")
    else:
        print(f"Plato no encontrado: {eliminar_plato}")

elif opciones == 4:
    print("Platos en el menu:")
    for plato in platos:
        print(f" - {plato}")

else:
    print("Opcion no valida.")