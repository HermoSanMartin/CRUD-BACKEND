from fastapi import FastAPI
from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

# 1. Creamos la aplicación (Esto soluciona el error de "app")
app = FastAPI()

# 2. Definimos nuestro estándar (Esto soluciona el error de "ApiResponse")
T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
    errors: Optional[list[Any]] = None

# 3. El endpoint estandarizado (Dejamos solo uno para evitar choques)
@app.get("/usuarios/{id}", response_model=ApiResponse[dict])
def get_user(id: int):
    user_data = {"id": id, "nombre": "Juan"}
    
    return ApiResponse(
        success=True,
        message="Usuario obtenido correctamente",
        data=user_data,
        errors=None
    )