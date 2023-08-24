class libro:
    def __init__(self,titulo,autor,genero,puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
        
libro1 = libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
libro2 = libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
libro3 = libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
libro4 = libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
libro5 = libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
libro6 = libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
libro7 = libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
libro8 = libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
libro9 = libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
libro10 = libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)  
      
lista_libro = [libro1,libro2,libro3,libro4,libro5,libro6,libro7,libro8,libro9,libro10]      

while True:
   
    print("1. Agregar Libro")
    print("2. Buscar Libros por Género")
    print("3. Recomendar Libro")
    print("4. Salir")
    
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        puntuacion = float(input("Puntuación: "))
        nuevo_libro = libro(titulo, autor, genero, puntuacion)
        lista_libro.append(nuevo_libro)
       
        
    elif opcion == 2:
        genero_buscado = input("Ingrese el género que desea buscar: ")
        libros_genero = [libro.titulo for libro in lista_libro if libro.genero == genero_buscado]
        if libros_genero:
            print(f"Libros en el género '{genero_buscado}':")
            for titulo_libro in libros_genero:
                print(titulo_libro)
        else:
            print(f"No se encontraron libros con el genero'{genero_buscado}'.")
            
    elif opcion == 3:
        recomendacion = input("Ingrese su género de interés: ")
        libros_genero = [libro for libro in lista_libro if libro.genero == recomendacion]
        if libros_genero:
            libro_recomendado = max(libros_genero, key=lambda libro: libro.puntuacion)
            print(f"Recomendación: {libro_recomendado.titulo} (Puntuación: {libro_recomendado.puntuacion})")
        else:
            print(f"No se encontraron libros en el género '{recomendacion}' para hacer una recomendación.")
            
    elif opcion == 4:
        print("Has salido del sistema")
        break
        
    else:
        print("Opción inválida. Ingrese otra opción.")       