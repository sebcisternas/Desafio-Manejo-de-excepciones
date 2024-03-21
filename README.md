# Desafio-Manejo-de-excepciones
Python 3.8

Este proyecto es parte de un desafío relacionado con el manejo de excepciones en Python. El objetivo del desafío era desarrollar una aplicación de galería de fotos e implementar un control para evitar que se modifiquen las dimensiones de una foto con valores que estén fuera de los límites permitidos.

## Descripción del Desafío

La tarea consistió en desarrollar una clase `Foto` que representara una foto en la galería. Se solicitó que esta clase incluyera métodos para establecer y obtener el alto y el ancho de la foto, así como la implementación de una excepción personalizada llamada `DimensionError`. Esta excepción debía lanzarse si se intentaba establecer un alto o ancho que estuviera por debajo de 1 o por encima de un valor máximo predefinido.

## Solución Implementada

Para resolver el desafío, se desarrolló la clase `Foto` con los métodos `alto` y `ancho` definidos como propiedades, lo que permitía una validación personalizada al establecer estos atributos. Se utilizó una excepción personalizada llamada `DimensionError` para manejar los errores relacionados con dimensiones fuera de los límites permitidos.

El archivo `error.py` contiene la definición de la clase `DimensionError`, que hereda de `Exception`. En esta clase se sobrescribió el método `__str__()` para personalizar el mensaje de la excepción, proporcionando información sobre las dimensiones proporcionadas y los valores máximos permitidos.

Además, en el archivo `foto.py`, se implementaron los métodos setter de `alto` y `ancho` de la clase `Foto`. Estos métodos lanzaban una excepción `DimensionError` si el nuevo valor estaba fuera de los límites permitidos.