def encontrar_palabra(frase):
    if "feliz" in frase:
        print(f"El emoji que te representa es: \U0001F603")
    if "triste" in frase:
        print(f"El emoji que te representa es: \U0001F622")


lista = []

def agregar_frase(frase):
    lista.append(frase)
    print(f"La frase se ha agregado correctamente. \n {lista}")