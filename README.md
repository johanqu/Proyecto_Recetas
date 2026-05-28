# RecetaAPI

API REST desarrollada con FastAPI que consume la API publica de TheMealDB y almacena recetas en MySQL. Incluye frontend web completo con Bootstrap.

## Tecnologias

- Python 3.x
- FastAPI
- SQLAlchemy
- MySQL
- Jinja2
- Bootstrap 5
- TheMealDB API
- pytest

## Estructura del proyecto

Proyecto_Recetas/
├── app/
│   ├── controllers/
│   ├── models/
│   ├── services/
│   ├── templates/
│   └── utils/
├── config/
├── tests/
├── main.py
├── database.sql
├── requirements.txt
└── README.md

## Instalacion

1. Clona el repositorio
```cmd
git clone https://github.com/johanqu/Proyecto_Recetas.git
```

2. Crea el entorno virtual
```cmd
python -m venv venv
venv\Scripts\activate
```

3. Instala las dependencias
```cmd
pip install -r requirements.txt
```

4. Crea el archivo .env con tus credenciales

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=recetario_db

5. Crea la base de datos en MySQL
```sql
CREATE DATABASE IF NOT EXISTS recetario_db;
```

6. Ejecuta el servidor
```cmd
uvicorn main:app --reload
```

7. Abre el navegador en

http://127.0.0.1:8000

## Paginas

| Pagina | URL | Descripcion |
|--------|-----|-------------|
| Inicio | / | Buscador y recetas populares |
| Explorar | /explorar | Explorar recetas por categoria |
| Mi Coleccion | /recetas | Recetas guardadas |
| Detalle | /recetas/{id} | Detalle de receta guardada |

## Endpoints API

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | /api/recetas | Obtener todas las recetas |
| GET | /api/recetas/{id} | Obtener receta por ID |
| POST | /api/recetas | Crear receta |
| PUT | /api/recetas/{id} | Actualizar receta |
| DELETE | /api/recetas/{id} | Eliminar receta |
| GET | /api/buscar/{nombre} | Buscar en TheMealDB |
| GET | /api/categoria/{categoria} | Filtrar por categoria |
| GET | /api/categorias | Ver categorias |
| POST | /api/guardar/{nombre} | Guardar receta desde MealDB |

## Tests
```cmd
pytest tests/test_api.py -v
```

## Autores
- Johan 
- Jawy
- Samuel