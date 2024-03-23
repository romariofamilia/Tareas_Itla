class Libro:
    def __init__(self, titulo, autor, genero, copias):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.copias = copias
        self.prestado = False

class Usuario:
    def __init__(self, nombre, email, id):
        self.nombre = nombre
        self.email = email
        self.id = id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros
        self.libros = {}

        # Diccionario para almacenar usuarios
        self.usuarios = {}

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la biblioteca.
        """
        if not all((libro.titulo, libro.autor, libro.genero, libro.copias)):
            raise ValueError("La informacion del libro es incompleta")
        
        self.libros[libro.titulo] = libro

    def buscar_libro(self, titulo="", autor="", genero=""):
        """
        Busca un libro por titulo, autor o género.
        """
        if not any((titulo, autor, genero)):
            raise ValueError("Debe proporcionar al menos un criterio de busqueda")

        libros_encontrados = []
        for libro in self.libros.values():
            if (titulo.lower() in libro.titulo.lower()) or \
               (autor.lower() in libro.autor.lower()) or \
               (genero.lower() in libro.genero.lower()):
                libros_encontrados.append(libro)
        return libros_encontrados

    def prestar_libro(self, usuario, libro):
        """
        Presta un libro a un usuario.
        """
        if libro.prestado:
            raise ValueError("El libro no esta disponible para prestar")

        libro.prestado = True
        usuario.libros_prestados.append(libro)

    def devolver_libro(self, usuario, libro):
        """
        Devuelve un libro prestado por un usuario.
        """
        if libro not in usuario.libros_prestados:
            raise ValueError("El usuario no tiene prestado este libro")

        libro.prestado = False
        usuario.libros_prestados.remove(libro)

    def mostrar_info_libro(self, libro):
        """
        Muestra información detallada de un libro
        """
        print(f"Titulo: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"Genero: {libro.genero}")
        print(f"Copias disponible: {libro.copias}")
        print(f"Prestado: {'Si' if libro.prestado else 'No'}")

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca
        """
        if not all((usuario.nombre, usuario.email, usuario.id)):
            raise ValueError("La informacion de usuario es incompleta")

        self.usuarios[usuario.id] = usuario


# Ejemplo de uso

biblioteca = Biblioteca()

usuario1 = Usuario('Romario', 'oooo@oooo.ooo', 1)

libro1 = Libro('El principito', 'Pablo Cohelo', 'Fantasia', 2)

biblioteca.agregar_libro(libro1)

biblioteca.prestar_libro(usuario1, libro1)


biblioteca.registrar_usuario(usuario1)


biblioteca.devolver_libro(usuario1, libro1)

biblioteca.mostrar_info_libro(libro1)

