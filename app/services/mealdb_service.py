import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1"

class MealDBService:
    
    def __init__(self):
        self.base_url = BASE_URL

    def __str__(self):
        return f"MealDBService conectado a {self.base_url}"

    def buscar_receta(self, nombre: str):
        try:
            response = requests.get(f"{self.base_url}/search.php?s={nombre}")
            
            if response.status_code != 200:
                return None
            
            data = response.json()
            
            if not data["meals"]:
                return None
                
            return data["meals"][0]
        
        except requests.exceptions.ConnectionError:
            raise Exception("Error de conexión con TheMealDB")
        
        except requests.exceptions.Timeout:
            raise Exception("La solicitud tardó demasiado")
        
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")

    def buscar_por_categoria(self, categoria: str):
        try:
            response = requests.get(f"{self.base_url}/filter.php?c={categoria}")
            
            if response.status_code != 200:
                return None
            
            data = response.json()
            
            if not data["meals"]:
                return None
                
            return data["meals"]
        
        except requests.exceptions.ConnectionError:
            raise Exception("Error de conexión con TheMealDB")
        
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")

    def obtener_categorias(self):
        try:
            response = requests.get(f"{self.base_url}/categories.php")
            
            if response.status_code != 200:
                return None
            
            data = response.json()
            return data["categories"]
        
        except Exception as e:
            raise Exception(f"Error inesperado: {str(e)}")
    
    
    def obtener_receta_random(self):
        try:
            response = requests.get(f"{self.base_url}/random.php")
            if response.status_code != 200:
                return None
            data = response.json()
            if not data["meals"]:
                return None
            return data["meals"][0]
        except Exception:
            return None