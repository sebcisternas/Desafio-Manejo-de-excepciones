from error import DimensionError

class Foto:
    MAX = 1000 # atributo de clase MAX para el tamaño máximo de la foto, 1000 es el valor dado.
    #constructor de foto
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, nuevo_alto):
        if nuevo_alto < 1 or nuevo_alto > self.MAX: # verifica si el nuevo alto está fuera de los límites permitidos
            # si esta fuera del rango de alto lanza una excepción DimensionError con un mensaje personalizado 
            raise DimensionError("El alto debe estar entre 1 y el máximo permitido.", dimension=nuevo_alto, maximo=self.MAX)
        self._alto = nuevo_alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        # si esta fuera del rango de ancho lanza una excepción DimensionError con un mensaje personalizado 
        if nuevo_ancho < 1 or nuevo_ancho > self.MAX:
            raise DimensionError("El ancho debe estar entre 1 y el máximo permitido.", dimension=nuevo_ancho, maximo=self.MAX)
        self._ancho = nuevo_ancho