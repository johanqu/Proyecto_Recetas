from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base
from app.models.base_model import BaseModel

class Receta(Base, BaseModel):
    __tablename__ = "recetas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    categoria = Column(String(100))
    area = Column(String(100))
    instrucciones = Column(Text)
    imagen = Column(String(500))
    fecha_guardado = Column(DateTime, default=datetime.utcnow)

    # Relación con ingredientes
    ingredientes = relationship("Ingrediente", back_populates="receta", cascade="all, delete")

    def __init__(self, nombre, categoria, area, instrucciones, imagen):
        # Llama al constructor de la clase madre
        BaseModel.__init__(self, nombre)
        self.nombre = nombre
        self.categoria = categoria
        self.area = area
        self.instrucciones = instrucciones
        self.imagen = imagen

    def __str__(self):
        return f"Receta: {self.nombre} | Categoria: {self.categoria} | Area: {self.area}"

    def __repr__(self):
        return f"Receta(id={self.id}, nombre={self.nombre})"

    # Polimorfismo - sobreescribe el metodo describir de BaseModel
    def describir(self):
        return f"Soy la receta '{self.nombre}' de la categoria {self.categoria} originaria de {self.area}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "area": self.area,
            "imagen": self.imagen,
            "fecha_guardado": str(self.fecha_guardado)
        }