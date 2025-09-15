from biblioteca import biblioteca

libro1 = biblioteca("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = biblioteca("El Principito", "Antoine de Saint-Exupéry", 96)
libro3 = biblioteca("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

print(libro1.mostrar_info())
print(libro2.mostrar_info())
print(libro3.mostrar_info())
print("PRUEBAS LIBRO GRANDE")
print(biblioteca.es_grande(libro1.paginas))  
print(biblioteca.es_grande(libro2.paginas))
print(biblioteca.total_libros())