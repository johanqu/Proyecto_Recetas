# RecetaAPI

API REST desarrollada con FastAPI que consume la API publica de TheMealDB y almacena recetas en MySQL.

## Tecnologias

- Python 3.x
- FastAPI
- SQLAlchemy
- MySQL
- TheMealDB API
- pytest

## Estructura del proyecto

Proyecto_Cocinaop/
├── app/
│ ├── controllers/
│ ├── models/
│ ├── services/
│ └── utils/
├── config/
├── tests/
├── main.py
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

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=recetario_db
```

5. Crea la base de datos en MySQL

```sql
CREATE DATABASE IF NOT EXISTS recetario_db;
```

6. Ejecuta el servidor

```cmd
uvicorn main:app --reload
```

## Endpoints

### Recetas

| Metodo | Endpoint      | Descripcion               |
| ------ | ------------- | ------------------------- |
| GET    | /recetas      | Obtener todas las recetas |
| GET    | /recetas/{id} | Obtener receta por ID     |
| POST   | /recetas      | Crear receta manual       |
| PUT    | /recetas/{id} | Actualizar receta         |
| DELETE | /recetas/{id} | Eliminar receta           |

### MealDB

| Metodo | Endpoint               | Descripcion                 |
| ------ | ---------------------- | --------------------------- |
| GET    | /buscar/{nombre}       | Buscar en TheMealDB         |
| GET    | /categoria/{categoria} | Filtrar por categoria       |
| GET    | /categorias            | Ver todas las categorias    |
| POST   | /guardar/{nombre}      | Guardar receta desde MealDB |

## Tests

```cmd
pytest tests/test_api.py -v
```

## Autores

- Johan
- Jawy
- Samuel
