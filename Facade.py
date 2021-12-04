"""Solución usando el patrón de diseño Facade"""

class Extraccion:
    def extraer_datos(self):
        print("extrayendo datos")

class Transformacion:
    def transformar_datos(self):
        print("transformando datos")

class Carga:
    def cargar_datos(self):
        print("cargando datos")

class Etl:
    def __init__(self):
        self.extraccion = Extraccion()
        self.transformacion = Transformacion()
        self.carga = Carga()

    def IniciarExtraccion(self):
        self.extraccion.extraer_datos()
        self.transformacion.transformar_datos()
        self.carga.cargar_datos()

if __name__ == "__main__":

    etl = Etl()
    etl.IniciarExtraccion()