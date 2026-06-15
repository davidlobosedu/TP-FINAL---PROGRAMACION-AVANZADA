
""" Consigna General  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Desarrollar una aplicación en Python denominada Sistema de Gestión de Biblioteca Digital. El
sistema deberá permitir administrar libros, usuarios y préstamos utilizando Programación
Orientada a Objetos. """

""" Requerimientos Funcionales  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/Gestión de Libros 
Datos mínimos: Título, Autor, ISBN, Año de publicación y Cantidad de páginas.
Operaciones mínimas: Alta, Modificación, Baja y Listado.
/Gestión de Usuarios
Datos mínimos: Nombre, Apellido, DNI y Correo electrónico.
Operaciones mínimas: Alta, Modificación, Baja y Listado.
/Gestión de Préstamos
Registrar préstamos, devoluciones y consultar préstamos activos.
Un libro no podrá prestarse si ya posee un préstamo activo.
Se deberá registrar fecha de préstamo y devolución.

Requerimientos Técnicos  - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -
• Implementar al menos una jerarquía de herencia.
• Implementar al menos un comportamiento polimórfico.
• Implementar al menos una relación de agregación.
• Implementar al menos una relación de composición.
• Implementar al menos un decorador propio e integrarlo dentro del sistema.
• Implementar una metaclase utilizando type o una clase derivada de type.
• Implementar al menos un patrón de diseño, debidamente justificado.

Diagrama UML  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
El trabajo deberá incluir un diagrama UML completo que represente: Clases Atributos Métodos
principales Relaciones de herencia Relaciones de agregación Relaciones de composición

Git y GitHub  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1. Crear un repositorio para el proyecto.
2. Invitar al docente mediante el usuario compudiego.
3. Mantener un historial de commits representativo del desarrollo realizado.
4. Utilizar mensajes de commit descriptivos.

README.md  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
El repositorio deberá contener obligatoriamente un archivo README.md con: Título del trabajo.
Breve descripción del sistema desarrollado. Nombre y apellido de todos los integrantes del grupo.
Instrucciones para ejecutar el proyecto. """

import datetime
# aca se genera el decorador propio que imprime fecha
# wrapper actua como un intermediario entre funciones originales y decoradas.
def auditar_accion(funcion):
    def wrapper(*args, **kwargs):
        hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{hora_actual}] Ejecutando acción: {funcion.__name__}...")
        # llama a la función original
        return funcion(*args, **kwargs)
    return wrapper 

# Se construye una metaclase con type.
# Acá} se crea una base genérica para cualquier material de la biblioteca.

def inicializar_material(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

def info_base(self):
    return f"Material genérico: {self.titulo}"

# Acá se crea la clase dinámicamente
MaterialBibliografico = type(
    'MaterialBibliografico', # Nombre de la clase
    (),                      # Clases de las que hereda (ninguna)
    {
        '__init__': inicializar_material, 
        'mostrar_info': info_base
    }
)

# Se crea una clase de composición para almacenar detalles técnicos de los libros.
# FichaTecnica no tiene sentido que exista suelta si no hay un libro.
class FichaTecnica:
    def __init__(self, isbn, anio, paginas):
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas

    def __str__(self):
        return f"ISBN: {self.isbn} | Año: {self.anio} | Páginas: {self.paginas}"
    
# Herencia: Libro hereda de MaterialBibliografico
class Libro(MaterialBibliografico):
    def __init__(self, titulo, autor, isbn, anio, paginas):
        # llamamos al inicializador de la clase padre (MaterialBibliografico)
        super().__init__(titulo, autor)
        
        # Composición: libro crea internamente su FichaTecnica.
        # Si libro se elimina, su ficha desaparece con él.
        self.ficha = FichaTecnica(isbn, anio, paginas)
        self.esta_prestado = False

    def mostrar_info(self):
        # acá se aplica polimorfismo cuando se sobreescribe "mostrar_info" de la clase padre.        
        estado = "[PRESTADO]" if self.esta_prestado else "[DISPONIBLE]"
        return f"Libro: {self.titulo} de {self.autor} | {self.ficha} -> {estado}"        

class Usuario:
    def __init__(self, nombre, apellido, dni, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo

        # Esta clase también tiene "mostrar_info", pero hace otra cosa (polimorfismo)
    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido} | DNI: {self.dni} | Correo: {self.correo}"
    
class Prestamo:
        # Un préstamo modela la relación entre un Libro y un Usuario.
        # Agregación; si el préstamo se elimina, el libro y el usuario conservan su propio ciclo de vida.
    def __init__(self, libro, usuario):
        self.libro = libro       # Agregación del objeto Libro
        self.usuario = usuario   # Agregación del objeto Usuario
        self.fecha_prestamo = datetime.datetime.now().strftime("%Y-%m-%d")
        self.fecha_devolucion = None

    def finalizar(self):
        self.fecha_devolucion = datetime.datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        estado = "Activo" if not self.fecha_devolucion else f"Devuelto el {self.fecha_devolucion}"
        return f"Préstamo: '{self.libro.titulo}' prestado a {self.usuario.nombre} ({estado})"
    
class GestorBiblioteca:
    _instancia = None
    # elegí el patrón singleton ya que puede existir una instancia de GestorBiblioteca.
    # método __new__ toma la creación del objeto, si ya existe devuelve el mismo en vez de crear uno nuevo.
    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(GestorBiblioteca, cls).__new__(cls, *args, **kwargs)
            # Inicializamos las listas de datos (en el caso de bases de datos en memoria)
            cls._instancia.libros = []
            cls._instancia.usuarios = []
            cls._instancia.prestamos = []
        return cls._instancia
    

    # alta, modificación, baja, listado de libros.
    # acá se aplica el decorador propio
    @auditar_accion 
    def alta_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado con éxito.")

    def listar_libros(self):
        print("\n--- CATÁLOGO DE LIBROS ---")
        for libro in self.libros:
            print(libro.mostrar_info())
            
    @auditar_accion
    def baja_libro(self, isbn):
        for libro in self.libros:
            if libro.ficha.isbn == isbn:
                if libro.esta_prestado:
                    print("Error: No se puede dar de baja un libro prestado.")
                    return
                self.libros.remove(libro)
                print(f"Libro '{libro.titulo}' eliminado.")
                return
        print("Libro no encontrado.")

    # alta, modificación, baja, listado de usuarios.
    @auditar_accion
    def alta_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' agregado con éxito.")

    def listar_usuarios(self):
        print("\n--- LISTA DE USUARIOS ---")
        for usuario in self.usuarios:
            print(usuario.mostrar_info())

    @auditar_accion
    def baja_usuario(self, dni):
        for u in self.usuarios:
            if u.dni == dni:
                self.usuarios.remove(u)
                print(f"Usuario con DNI {dni} eliminado.")
                return
        print("Usuario no encontrado.")

    # Registrar préstamos, devoluciones y consultar préstamos .
    @auditar_accion
    def registrar_prestamo(self, isbn_libro, dni_usuario):
        # Buscamos los objetos
        libro_encontrado = next((l for l in self.libros if l.ficha.isbn == isbn_libro), None)
        usuario_encontrado = next((u for u in self.usuarios if u.dni == dni_usuario), None)

        if not libro_encontrado or not usuario_encontrado:
            print("Error: libro o usuario no existen.")
            return

        if libro_encontrado.esta_prestado:
            print(f"Error: el libro '{libro_encontrado.titulo}' tiene un préstamo activo.")
            return

        # se crea el préstamo pasando los objetos (agregación)
        nuevo_prestamo = Prestamo(libro_encontrado, usuario_encontrado)
        self.prestamos.append(nuevo_prestamo)
        libro_encontrado.esta_prestado = True
        print(f"Préstamo registrado exitosamente.")

    @auditar_accion
    def registrar_devolucion(self, isbn_libro):
        for p in self.prestamos:
            if p.libro.ficha.isbn == isbn_libro and p.fecha_devolucion is None:
                p.finalizar()
                p.libro.esta_prestado = False
                print(f"Devolución de '{p.libro.titulo}' registrada exitosamente.")
                return
        print("Error: no hay préstamos activos para ese libro.")

    def consultar_prestamos_activos(self):
        print("\n--- PRÉSTAMOS ACTIVOS ---")
        activos = [p for p in self.prestamos if p.fecha_devolucion is None]
        if not activos:
            print("No hay préstamos en curso.")
        else:
            for p in activos:
                print(p)