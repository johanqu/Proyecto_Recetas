from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.receta import Receta
from app.models.ingrediente import Ingrediente
from app.utils.error_handler import receta_no_encontrada, error_servidor
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Schema de entrada
class RecetaSchema(BaseModel):
    nombre: str
    categoria: Optional[str] = None
    area: Optional[str] = None
    instrucciones: Optional[str] = None
    imagen: Optional[str] = None

# GET todas las recetas
@router.get("/recetas")
def obtener_recetas(db: Session = Depends(get_db)):
    try:
        recetas = db.query(Receta).all()
        return {"total": len(recetas), "recetas": [
            {
                "id": r.id,
                "nombre": r.nombre,
                "categoria": r.categoria,
                "area": r.area,
                "imagen": r.imagen,
                "fecha_guardado": r.fecha_guardado
            } for r in recetas
        ]}
    except Exception:
        error_servidor()

# GET receta por ID
@router.get("/recetas/{id}")
def obtener_receta(id: int, db: Session = Depends(get_db)):
    receta = db.query(Receta).filter(Receta.id == id).first()
    if not receta:
        receta_no_encontrada(id)
    return receta

# POST crear receta
@router.post("/recetas")
def crear_receta(data: RecetaSchema, db: Session = Depends(get_db)):
    try:
        receta = Receta(
            nombre=data.nombre,
            categoria=data.categoria,
            area=data.area,
            instrucciones=data.instrucciones,
            imagen=data.imagen
        )
        db.add(receta)
        db.commit()
        db.refresh(receta)
        return {"mensaje": "Receta creada exitosamente", "id": receta.id}
    except Exception:
        error_servidor()

# PUT actualizar receta
@router.put("/recetas/{id}")
def actualizar_receta(id: int, data: RecetaSchema, db: Session = Depends(get_db)):
    receta = db.query(Receta).filter(Receta.id == id).first()
    if not receta:
        receta_no_encontrada(id)
    receta.nombre = data.nombre
    receta.categoria = data.categoria
    receta.area = data.area
    receta.instrucciones = data.instrucciones
    receta.imagen = data.imagen
    db.commit()
    return {"mensaje": "Receta actualizada exitosamente"}

# DELETE eliminar receta
@router.delete("/recetas/{id}")
def eliminar_receta(id: int, db: Session = Depends(get_db)):
    receta = db.query(Receta).filter(Receta.id == id).first()
    if not receta:
        receta_no_encontrada(id)
    db.delete(receta)
    db.commit()
    return {"mensaje": "Receta eliminada exitosamente"}