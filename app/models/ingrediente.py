from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from app.models.base_model import BaseModel

class Ingrediente(Base, BaseModel):
    __tablename__ = "ingredientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    medida = Column(String(100))
    id_receta = Column(Integer, ForeignKey("recetas.id"), nullable=False)

    # Relación con receta
    receta = relationship("Receta", back_populates="ingredientes")

    def __init__(self, nombre, medida, id_receta):
        # Llama al constructor de la clase madre
        BaseModel.__init__(self, nombre)
        self.nombre = nombre
        self.medida = medida
        self.id_receta = id_receta

    def __str__(self):
        return f"Ingrediente: {self.nombre} | Medida: {self.medida}"

    def __repr__(self):
        return f"Ingrediente(id={self.id}, nombre={self.nombre})"

    # Polimorfismo - sobreescribe el metodo describir de BaseModel
    def describir(self):
        return f"Soy el ingrediente '{self.nombre}' con medida {self.medida}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "medida": self.medida,
            "id_receta": self.id_receta
        }