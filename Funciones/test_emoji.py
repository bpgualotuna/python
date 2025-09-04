import emoji

cantidad_frase = int(input("¿Cuantas frases deseas ingresar? \n"))

for i in range(cantidad_frase):
    frase = input(f"Ingrese la frase {i+1}: \n")
    emoji.encontrar_palabra(frase)
    emoji.agregar_frase(frase)
    

