
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
        # Llamamos al inicializador de la clase padre (MaterialBibliografico)
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