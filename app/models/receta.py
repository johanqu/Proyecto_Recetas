from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base

class Receta(Base):
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
        self.nombre = nombre
        self.categoria = categoria
        self.area = area
        self.instrucciones = instrucciones
        self.imagen = imagen

    def __str__(self):
        return f"Receta: {self.nombre} | Categoría: {self.categoria} | Área: {self.area}"