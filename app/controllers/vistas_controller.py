from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.receta import Receta
from app.services.mealdb_service import MealDBService
import requests as req

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
service = MealDBService()

# Pagina principal
@router.get("/", response_class=HTMLResponse)
def index(request: Request, nombre: str = None, db: Session = Depends(get_db)):
    receta = None
    error = None
    recetas_populares = []

    for _ in range(4):
        r = service.obtener_receta_random()
        if r:
            recetas_populares.append(r)

    if nombre:
        try:
            receta = service.buscar_receta(nombre)
            if not receta:
                error = f"No se encontro ninguna receta con el nombre '{nombre}'"
        except Exception:
            error = "Error al conectar con TheMealDB"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "receta": receta,
            "error": error,
            "recetas_populares": recetas_populares
        }
    )

# Pagina explorar recetas
@router.get("/explorar", response_class=HTMLResponse)
def explorar(request: Request, categoria: str = None):
    recetas = []
    categorias = service.obtener_categorias()

    if categoria:
        resultado = service.buscar_por_categoria(categoria)
        if resultado:
            recetas = resultado
    else:
        for _ in range(12):
            r = service.obtener_receta_random()
            if r:
                recetas.append(r)

    return templates.TemplateResponse(
        request=request,
        name="explorar.html",
        context={
            "recetas": recetas,
            "categorias": categorias,
            "categoria_actual": categoria
        }
    )

# Detalle de receta desde explorar
@router.get("/explorar/{id_meal}", response_class=HTMLResponse)
def detalle_explorar(request: Request, id_meal: str):
    try:
        response = req.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id_meal}")
        data = response.json()
        if not data["meals"]:
            return RedirectResponse(url="/explorar")
        receta = data["meals"][0]

        ingredientes = []
        for i in range(1, 21):
            nombre_ing = receta.get(f"strIngredient{i}")
            medida_ing = receta.get(f"strMeasure{i}")
            if nombre_ing and nombre_ing.strip():
                ingredientes.append({"nombre": nombre_ing, "medida": medida_ing})

        return templates.TemplateResponse(
            request=request,
            name="detalle_explorar.html",
            context={
                "receta": receta,
                "ingredientes": ingredientes
            }
        )
    except Exception:
        return RedirectResponse(url="/explorar")

# Lista de recetas guardadas
@router.get("/recetas", response_class=HTMLResponse)
def lista_recetas(request: Request, db: Session = Depends(get_db)):
    recetas = db.query(Receta).all()
    return templates.TemplateResponse(
        request=request,
        name="recetas.html",
        context={"recetas": recetas}
    )

# Detalle de una receta guardada
@router.get("/recetas/{id}", response_class=HTMLResponse)
def detalle_receta(request: Request, id: int, db: Session = Depends(get_db)):
    receta = db.query(Receta).filter(Receta.id == id).first()
    if not receta:
        return RedirectResponse(url="/recetas")
    return templates.TemplateResponse(
        request=request,
        name="detalle.html",
        context={"receta": receta}
    )

# Guardar receta desde MealDB
@router.post("/guardar")
def guardar_receta(nombre: str = Form(...), db: Session = Depends(get_db)):
    try:
        data = service.buscar_receta(nombre)
        if not data:
            return RedirectResponse(url="/", status_code=303)

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

        from app.models.ingrediente import Ingrediente
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
        db.commit()

    except Exception:
        pass

    return RedirectResponse(url="/recetas", status_code=303)

# Eliminar receta
@router.post("/recetas/{id}/eliminar")
def eliminar_receta(id: int, db: Session = Depends(get_db)):
    receta = db.query(Receta).filter(Receta.id == id).first()
    if receta:
        db.delete(receta)
        db.commit()
    return RedirectResponse(url="/recetas", status_code=303)