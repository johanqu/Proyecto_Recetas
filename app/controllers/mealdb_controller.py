from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.receta import Receta
from app.models.ingrediente import Ingrediente
from app.services.mealdb_service import MealDBService
from app.utils.error_handler import receta_no_encontrada_api, error_conexion_api, error_servidor

router = APIRouter()
service = MealDBService()

# GET buscar receta en MealDB por nombre
@router.get("/buscar/{nombre}")
def buscar_receta(nombre: str):
    try:
        receta = service.buscar_receta(nombre)
        if not receta:
            receta_no_encontrada_api(nombre)
        return receta
    except Exception as e:
        if "conexión" in str(e):
            error_conexion_api()
        error_servidor()

# GET filtrar recetas por categoría
@router.get("/categoria/{categoria}")
def buscar_por_categoria(categoria: str):
    try:
        recetas = service.buscar_por_categoria(categoria)
        if not recetas:
            receta_no_encontrada_api(categoria)
        return {"total": len(recetas), "recetas": recetas}
    except Exception as e:
        if "conexión" in str(e):
            error_conexion_api()
        error_servidor()

# GET obtener todas las categorías disponibles
@router.get("/categorias")
def obtener_categorias():
    try:
        categorias = service.obtener_categorias()
        if not categorias:
            error_servidor()
        return {"total": len(categorias), "categorias": categorias}
    except Exception:
        error_conexion_api()

# POST buscar en MealDB y guardar en MySQL
@router.post("/guardar/{nombre}")
def guardar_receta(nombre: str, db: Session = Depends(get_db)):
    try:
        # Busca en MealDB
        data = service.buscar_receta(nombre)
        if not data:
            receta_no_encontrada_api(nombre)

        # Crea la receta en MySQL
        receta = Receta(
            nombre=data.get("strMeal"),
            categoria=data.get("strCategory"),
            area=data.get("strArea"),
            instrucciones=data.get("strInstructions"),
            imagen=data.get("strMealThumb")
        )
        db.add(receta)
        db.commit()
        db.refresh(receta)

        # Extrae y guarda los ingredientes
        ingredientes_guardados = []
        for i in range(1, 21):
            nombre_ing = data.get(f"strIngredient{i}")
            medida_ing = data.get(f"strMeasure{i}")
            if nombre_ing and nombre_ing.strip():
                ingrediente = Ingrediente(
                    nombre=nombre_ing,
                    medida=medida_ing,
                    id_receta=receta.id
                )
                db.add(ingrediente)
                ingredientes_guardados.append(nombre_ing)

        db.commit()

        return {
            "mensaje": f"Receta '{receta.nombre}' guardada exitosamente",
            "id": receta.id,
            "ingredientes_guardados": len(ingredientes_guardados)
        }

    except Exception as e:
        if "conexión" in str(e):
            error_conexion_api()
        error_servidor()