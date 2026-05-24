from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Ingrediente(Base):
    __tablename__ = "ingredientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    medida = Column(String(100))
    id_receta = Column(Integer, ForeignKey("recetas.id"), nullable=False)

    # Relación con receta
    receta = relationship("Receta", back_populates="ingredientes")

    def __init__(self, nombre, medida, id_receta):
        self.nombre = nombre
        self.medida = medida
        self.id_receta = id_receta

    def __str__(self):
        return f"Ingrediente: {self.nombre} | Medida: {self.medida}"