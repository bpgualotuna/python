import random

destino = int(input("Ingrese el Numero de su destino \n1.-Ecuador\n2.-Colombia\n3.-Peru\n"))

velocidad = random.randint(1,100)

if destino == 1:
    print("Usted ha elegido Ecuador")
    zona = int(input("Ingrese la zona en la que viaja \n1.-Urbana\n2.-Rural\n3.-Perimetral\n"))
    if zona == 1:
        if velocidad < 10:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Urbana")
        elif velocidad >= 10 and velocidad <= 50:
            print(f"Su velocidad esta dentro de los limites de la Zona Urbana--> {velocidad} km/h")
        elif velocidad >= 51:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Urbana")
    elif zona == 2:
        if velocidad < 51:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Rural")
        elif velocidad >= 51 and velocidad <= 70:
            print(f"Su velocidad esta dentro de los limites de la Zona Rural--> {velocidad} km/h")
        elif velocidad > 70:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Rural")
    elif zona == 3:
        if velocidad < 71:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Perimetral")
        elif velocidad >= 71 and velocidad < 90:
            print(f"Su velocidad esta dentro de los limites de la Zona Perimetral--> {velocidad} km/h")
        elif velocidad >= 90:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Perimetral")
elif destino == 2:
    print("Usted ha elegido Colombia")
    zona = int(input("Ingrese la zona en la que viaja \n1.-Urbana\n2.-Rural\n3.-Perimetral\n"))
    if zona == 1:
        if velocidad < 10:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Urbana")
        elif velocidad >= 10 and velocidad <= 30:
            print(f"Su velocidad esta dentro de los limites de la Zona Urbana--> {velocidad} km/h")
        elif velocidad > 30:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Urbana")
    elif zona == 2:
        if velocidad < 31:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Rural")
        elif velocidad >= 31 and velocidad <= 80:
            print(f"Su velocidad esta dentro de los limites de la Zona Rural--> {velocidad} km/h")
        elif velocidad > 80:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Rural")
    elif zona == 3:
        if velocidad < 81:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Perimetral")
        elif velocidad >= 80 and velocidad <= 100:
            print(f"Su velocidad esta dentro de los limites de la Zona Perimetral--> {velocidad} km/h")
        elif velocidad > 100:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Perimetral")
elif destino == 3:
    print("Usted ha elegido Peru")
    zona = int(input("Ingrese la zona en la que viaja \n1.-Urbana\n2.-Rural\n3.-Perimetral\n"))
    if zona == 1:
        if velocidad < 10:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Urbana")
        elif velocidad >= 10 and velocidad <= 40:
            print(f"Su velocidad esta dentro de los limites de la Zona Urbana--> {velocidad} km/h")
        elif velocidad > 40:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Urbana")
    elif zona == 2:
        if velocidad < 41:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Rural")
        elif velocidad >= 41 and velocidad <= 60:
            print(f"Su velocidad esta dentro de los limites de la Zona Rural--> {velocidad} km/h")
        elif velocidad > 60:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Rural")
    elif zona == 3:
        if velocidad < 61:
            print(f"Su velocidad es de {velocidad} km/h, esta por debajo de los limites de la Zona Perimetral")
        elif velocidad >= 61 and velocidad <= 120:
            print(f"Su velocidad esta dentro de los limites de la Zona Perimetral--> {velocidad} km/h")
        elif velocidad > 120:
            print(f"Su velocidad es de {velocidad} km/h, excede los limites de la Zona Perimetral")
else:
    print("Destino no valido")