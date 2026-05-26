import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TEST 1 — Verificar que el servidor responde correctamente
def test_inicio():
    response = client.get("/")
    assert response.status_code == 200

# TEST 2 — Verificar que se pueden obtener las recetas via API
def test_obtener_recetas():
    response = client.get("/api/recetas")
    assert response.status_code == 200
    assert "recetas" in response.json()
    assert "total" in response.json()

# TEST 3 — Verificar búsqueda en TheMealDB
def test_buscar_receta_mealdb():
    response = client.get("/api/buscar/pasta")
    assert response.status_code == 200
    assert "strMeal" in response.json()

# TEST 4 — Verificar receta no encontrada
def test_receta_no_encontrada():
    response = client.get("/api/recetas/9999")
    assert response.status_code == 404

# TEST 5 — Verificar obtener categorías
def test_obtener_categorias():
    response = client.get("/api/categorias")
    assert response.status_code == 200
    assert "categorias" in response.json()