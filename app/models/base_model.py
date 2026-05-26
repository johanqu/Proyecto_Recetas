from datetime import datetime

class BaseModel:
    """Clase base de la que heredan todos los modelos del sistema"""

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__fecha_creacion = datetime.utcnow()

    # Encapsulamiento - getter y setter para nombre
    @property
    def nombre_modelo(self):
        return self.__nombre

    @nombre_modelo.setter
    def nombre_modelo(self, valor: str):
        if not valor or len(valor.strip()) == 0:
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = valor.strip()

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    # Metodo especial
    def __str__(self):
        return f"Modelo: {self.__nombre} | Creado: {self.__fecha_creacion}"

    def __repr__(self):
        return f"BaseModel(nombre={self.__nombre})"

    # Metodo que sera sobreescrito por las clases hijas (polimorfismo)
    def describir(self):
        return f"Soy un modelo base llamado {self.__nombre}"

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "fecha_creacion": str(self.__fecha_creacion)
        }