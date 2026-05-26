from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from config.database import engine, Base
from app.controllers import receta_controller, mealdb_controller, ingrediente_controller, vistas_controller

# Crea todas las tablas en MySQL automáticamente
Base.metadata.create_all(bind=engine)

# Crea la instancia de FastAPI
app = FastAPI(
    title="RecetaAPI",
    description="API para gestionar recetas consumiendo TheMealDB",
    version="1.0.0"
)

# Registra los controladores
app.include_router(vistas_controller.router, tags=["Vistas"])
app.include_router(receta_controller.router, prefix="/api", tags=["Recetas"])
app.include_router(mealdb_controller.router, prefix="/api", tags=["MealDB"])
app.include_router(ingrediente_controller.router, prefix="/api", tags=["Ingredientes"])