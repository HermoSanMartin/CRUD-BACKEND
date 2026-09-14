from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.routers import coleccionistas_router, obras_router

app = FastAPI(
    title="API REST - Galería de Arte de Lujo",
    description="Backend en 5 capas para la gestión de arte, coleccionistas y ventas.",
    version="1.0.0"
)

# Manejador de errores estandarizado para validaciones (HTTP 422)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Los datos enviados no cumplen con el formato requerido",
                "details": exc.errors()
            }
        }
    )

# Manejador de excepciones genéricas de negocio (HTTP 400)
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": "BUSINESS_RULE_VIOLATION",
                "message": str(exc),
                "details": []
            }
        }
    )

# Registro de rutas por controlador
app.include_router(coleccionistas_router.router)
app.include_router(obras_router.router)

@app.get("/")
def root():
    return {"message": "API REST Galería de Arte activa. Revisa /docs para Swagger UI"}