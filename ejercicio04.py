class Libro:
    def __init__(self, titulo, autor, anio, disponible=True):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._disponible = disponible

    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor

    def prestar_libro(self):
        if self._disponible:
            self._disponible = False
            print(f"El libro '{self._titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self._titulo}' ya se encuentra prestado.")
    def devolver_libro(self):
        if not self._disponible:
            self._disponible = True
            print(f"El libro '{self._titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self._titulo}' ya estaba en la biblioteca.")
    def mostrar_datos(self):
        estado = "Disponible" if self._disponible else "Prestado"
        print(f"Titulo: {self._titulo} | Autor: {self._autor} | Año: {self._anio} | Estado: {estado}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamanoMB):
        super().__init__(titulo, autor, anio, disponible=True)
        self._formato = formato
        self._tamanoMB = tamanoMB

    def prestar_libro(self):
        print(f"El libro digital '{self._titulo}' ({self._formato}) se ha descargado.")
    def mostrar_datos(self):
        print(f"Titulo: {self._titulo} | Autor: {self._autor} | [DIGITAL {self._formato} - {self._tamanoMB}MB]")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    def listar_libros(self):
        print("\nCatálogo de libros")
        for libro in self.libros:
            libro.mostrar_datos()
    def buscar_por_autor(self, autor_buscado):
        encontrados = []
        for libro in self.libros:
            if libro.autor == autor_buscado:
                encontrados.append(libro)
        return encontrados
    def buscar_por_titulo(self, titulo_buscado):
        for libro in self.libros:
            if libro.titulo == titulo_buscado:
                return libro
        return None
    def prestar_libro(self, titulo_buscado):
        encontrado = False
        for libro in self.libros:
            if libro.titulo == titulo_buscado:
                libro.prestar_libro()
                encontrado = True
                break     
        if not encontrado:
            print(f"No se encontró el libro titulado: '{titulo_buscado}'")

libro1 = Libro("Cien Anios de Soledad", "Gabriel Garcia Marquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
libro4 = LibroDigital("El Principito", "Antoine de Saint-Exupery", 1943, "PDF", 2)
libro5 = LibroDigital("Sapiens", "Yuval Noah Harari", 2011, "EPUB", 5)

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

biblioteca.listar_libros()

print("\nPrestar libro fisico")
biblioteca.prestar_libro("Cien Anios de Soledad")

print("\nIntentar prestar libro ocupado")
biblioteca.prestar_libro("Cien Anios de Soledad")

print("\nPrestar libro digital")
for i in range(5):
    biblioteca.prestar_libro("El Principito")

print("\nBúsqueda por autor")
resultados_busqueda = biblioteca.buscar_por_autor("George Orwell")
for libro in resultados_busqueda:
    libro.mostrar_datos()