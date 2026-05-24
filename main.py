from fastapi import FastAPI
from config.database import engine, Base
from app.controllers import receta_controller, mealdb_controller

# Crea todas las tablas en MySQL automáticamente
Base.metadata.create_all(bind=engine)

# Crea la instancia de FastAPI
app = FastAPI(
    title="RecetaAPI",
    description="API para gestionar recetas consumiendo TheMealDB",
    version="1.0.0"
)

# Registra los controladores
app.include_router(receta_controller.router, tags=["Recetas"])
app.include_router(mealdb_controller.router, tags=["MealDB"])

# Endpoint raíz
@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a RecetaAPI",
        "docs": "/docs",
        "version": "1.0.0"
    }