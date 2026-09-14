from typing import List, Optional, Literal
from datetime import datetime
lienlafelipe
from pydantic import BaseModel, EmailStr, Field

# --- ESQUEMAS ARTISTA ---
class ArtistaCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    nacionalidad: str = Field(..., min_length=2)
    estilo_principal: str
    obras_creadas: int = Field(default=0, ge=0)

class ArtistaResponse(ArtistaCreate):
    id: int

# --- ESQUEMAS COLECCIONISTA ---
from pydantic import BaseModel, EmailStr, Field


#artistas

class ArtistaCreate(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    nacionalidad: str = Field(..., min_length=2)
    estilo_principal: str = Field(..., min_length=2, max_length=100)
    obras_creadas: int = Field(default=0, ge=0)


class ArtistaResponse(ArtistaCreate):
    id: int


#coleccionistas

main
class ColeccionistaCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    correo: EmailStr
    presupuesto: float = Field(..., gt=0)
    es_vip: bool = False

lienlafelipe
class ColeccionistaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)

class ColeccionistaUpdate(BaseModel):
    nombre: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100
    )
main
    correo: Optional[EmailStr] = None
    presupuesto: Optional[float] = Field(None, gt=0)
    es_vip: Optional[bool] = None

lienlafelipe
class ColeccionistaResponse(ColeccionistaCreate):
    id: int

# --- ESQUEMAS OBRA DE ARTE ---
class ObraArteCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=80)
    precio: float = Field(..., gt=0)
    estado: Literal["DISPONIBLE", "RESERVADA", "VENDIDA"] = "DISPONIBLE"
    anio_creacion: int = Field(..., ge=1000, le=2026)
    artista_id: int

class ColeccionistaResponse(ColeccionistaCreate):
    id: int


#obras

class ObraArteCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=80)
    precio: float = Field(..., gt=0)

    estado: Literal[
        "DISPONIBLE",
        "RESERVADA",
        "VENDIDA"
    ] = "DISPONIBLE"

    anio_creacion: int = Field(..., ge=1000, le=2026)

    artista_id: int = Field(..., gt=0)

main

class ObraArteResponse(ObraArteCreate):
    id: int

lienlafelipe
# --- ESQUEMAS VENTA ---
class VentaCreate(BaseModel):
    coleccionista_id: int
    obra_id: int

#venta

class VentaCreate(BaseModel):
    coleccionista_id: int = Field(..., gt=0)
    obra_id: int = Field(..., gt=0)

main

class VentaResponse(BaseModel):
    id: int
    coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: datetime

lienlafelipe
# --- PAGINACIÓN ---
class PaginatedObrasResponse(BaseModel):
    items: List[ObraArteResponse]
    total: int
    pagina: int
    limite: int
    total_paginas: int

#paginacion

class PaginatedObrasResponse(BaseModel):
    items: List[ObraArteResponse]
    total: int = Field(..., ge=0)
    pagina: int = Field(..., ge=1)
    limite: int = Field(..., gt=0)
    total_paginas: int = Field(..., ge=0)
main
