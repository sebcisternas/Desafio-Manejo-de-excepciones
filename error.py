class DimensionError(Exception):
    def __init__(self, mensaje, dimension, maximo):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            mensaje = f"Error: {self.mensaje}."
            if self.dimension is not None:
                mensaje += f" La dimensión proporcionada es {self.dimension}."
            if self.maximo is not None:
                mensaje += f" El valor máximo permitido es {self.maximo}."
            return mensaje