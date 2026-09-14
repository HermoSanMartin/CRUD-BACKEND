lienlafelipe
# API REST - Galería de Arte de Lujo

API REST desarrollada con **FastAPI** y **Pydantic** para la gestión en memoria de obras de arte, coleccionistas, artistas y transacciones de venta de alto valor. Diseñada bajo una arquitectura limpia en 5 capas con separación estricta de responsabilidades.

---

# Información del Proyecto y Colaboración
* **Repositorio:** `CRUD-BACKEND`
* **Rama de Trabajo:** `lienlafelipe`
* **Autor:** Felipe Lienlaf
* **Evaluación:** Proyecto Backend E01 - Desarrollo Individual / Grupal

---

# Tecnologías y Herramientas
* **Lenguaje:** Python 3.10+
* **Framework Web:** FastAPI
* **Validaciones de Datos:** Pydantic v2 (uso de `Literal`, `EmailStr`, `Field`, `datetime`)
* **Servidor ASGI:** Uvicorn
* **Control de Versiones:** Git & GitHub

---

# Estructura del Proyecto (Arquitectura en 5 Capas)

El proyecto sigue estrictamente la arquitectura requerida en la pauta de evaluación:

```text
CRUD-BACKEND/
├── app/
│   ├── domain/           # Entidades base y tipos del dominio (models.py)
│   ├── repositories/     # Persistencia y almacenamiento en memoria (memory_repository.py)
│   ├── routers/          # Controladores HTTP y rutas FastAPI (coleccionistas_router.py, obras_router.py)
│   ├── schemas/          # DTOs y esquemas de validación Pydantic (schemas.py)
│   ├── services/         # Casos de uso y reglas de negocio (gallery_service.py)
│   └── main.py           # Configuración principal y manejador unificado de errores
├── tests_manual/         # Colección de pruebas para Thunder Client / Postman
│   └── coleccion_pruebas.json
├── README.md             # Documentación técnica del proyecto
└── requirements.txt      # Librerías y dependencias
=======
main
