# Sistema de Gestión de Biblioteca Digital

Descripción del Sistema
Este proyecto consiste en una aplicación desarrollada en Python usando el paradigma de POO.
Su objetivo principal es centralizar y administrar el catálogo de libros, el registro de usuarios y 
la gestión de préstamos (con sus respectivas devoluciones y fechas).

El código cumple con los requerimientos técnicos pedidos , confirmando el uso de:
Herencia y Polimorfismo: A través de la clase abstracta `MaterialBiblioteca` y su subclase `Libro`.
Relaciones de Composición y Agregación: Aplicadas para vincular el registro de fechas con los 
préstamos (vida ligada) y para que la biblioteca agrupe usuarios y libros (vida independiente).
Metaclases: Implementación mediante `type()` para crear la clase base `EntidadIdentificable` 
encargada de gestionar los identificadores únicos.
Decoradores: Uso del decorador propio `@auditoria_log` que envuelve las funciones y registra 
la fecha/hora exacta de cada operación.
Patrones de Diseño: Aplicación del patrón creacional Singleton para garantizar que exista una única
instancia global del sistema gestor (`BibliotecaDigital`).

Integrantes del grupo:
David Lobos


Instrucciones para ejecutar el proyecto
1. Verificar tener instalado Python 3 en su computadora.
2. Clonar este repositorio en su entorno local usando Git o descargue directamente
   los archivos del proyecto.
3. Abrir una terminal o línea de comandos y navegar hasta el directorio raíz del proyecto
    usando el comando `cd` (por ejemplo, `cd carpeta_del_proyecto`).
4. Ejecutar el archivo principal del sistema (confirmando que el código se encuentra en un
   archivo llamado `main.py` ) mediante el siguiente comando:
   ```bash
   python main.py
