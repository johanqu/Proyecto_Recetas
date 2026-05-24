from fastapi import HTTPException

def receta_no_encontrada(id: int):
    raise HTTPException(
        status_code=404,
        detail=f"No se encontró ninguna receta con el ID {id}"
    )

def ingrediente_no_encontrado(id: int):
    raise HTTPException(
        status_code=404,
        detail=f"No se encontró ningún ingrediente con el ID {id}"
    )

def receta_no_encontrada_api(nombre: str):
    raise HTTPException(
        status_code=404,
        detail=f"No se encontró '{nombre}' en TheMealDB"
    )

def error_conexion_api():
    raise HTTPException(
        status_code=503,
        detail="No se pudo conectar con TheMealDB, intenta más tarde"
    )

def error_servidor():
    raise HTTPException(
        status_code=500,
        detail="Error interno del servidor"
    )