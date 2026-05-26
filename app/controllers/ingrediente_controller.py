from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.ingrediente import Ingrediente
from app.utils.error_handler import ingrediente_no_encontrado, error_servidor
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Schema de entrada
class IngredienteSchema(BaseModel):
    nombre: str
    medida: Optional[str] = None
    id_receta: int

# GET todos los ingredientes
@router.get("/ingredientes")
def obtener_ingredientes(db: Session = Depends(get_db)):
    try:
        ingredientes = db.query(Ingrediente).all()
        return {"total": len(ingredientes), "ingredientes": [
            {
                "id": i.id,
                "nombre": i.nombre,
                "medida": i.medida,
                "id_receta": i.id_receta
            } for i in ingredientes
        ]}
    except Exception:
        error_servidor()

# GET ingrediente por ID
@router.get("/ingredientes/{id}")
def obtener_ingrediente(id: int, db: Session = Depends(get_db)):
    ingrediente = db.query(Ingrediente).filter(Ingrediente.id == id).first()
    if not ingrediente:
        ingrediente_no_encontrado(id)
    return ingrediente

# POST crear ingrediente
@router.post("/ingredientes")
def crear_ingrediente(data: IngredienteSchema, db: Session = Depends(get_db)):
    try:
        ingrediente = Ingrediente(
            nombre=data.nombre,
            medida=data.medida,
            id_receta=data.id_receta
        )
        db.add(ingrediente)
        db.commit()
        db.refresh(ingrediente)
        return {"mensaje": "Ingrediente creado exitosamente", "id": ingrediente.id}
    except Exception:
        error_servidor()

# PUT actualizar ingrediente
@router.put("/ingredientes/{id}")
def actualizar_ingrediente(id: int, data: IngredienteSchema, db: Session = Depends(get_db)):
    ingrediente = db.query(Ingrediente).filter(Ingrediente.id == id).first()
    if not ingrediente:
        ingrediente_no_encontrado(id)
    ingrediente.nombre = data.nombre
    ingrediente.medida = data.medida
    ingrediente.id_receta = data.id_receta
    db.commit()
    return {"mensaje": "Ingrediente actualizado exitosamente"}

# DELETE eliminar ingrediente
@router.delete("/ingredientes/{id}")
def eliminar_ingrediente(id: int, db: Session = Depends(get_db)):
    ingrediente = db.query(Ingrediente).filter(Ingrediente.id == id).first()
    if not ingrediente:
        ingrediente_no_encontrado(id)
    db.delete(ingrediente)
    db.commit()
    return {"mensaje": "Ingrediente eliminado exitosamente"}