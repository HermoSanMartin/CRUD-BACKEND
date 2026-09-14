from typing import List, Optional, Literal
from datetime import datetime
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
class ColeccionistaCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    correo: EmailStr
    presupuesto: float = Field(..., gt=0)
    es_vip: bool = False

class ColeccionistaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=100)
    correo: Optional[EmailStr] = None
    presupuesto: Optional[float] = Field(None, gt=0)
    es_vip: Optional[bool] = None

class ColeccionistaResponse(ColeccionistaCreate):
    id: int

# --- ESQUEMAS OBRA DE ARTE ---
class ObraArteCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=80)
    precio: float = Field(..., gt=0)
    estado: Literal["DISPONIBLE", "RESERVADA", "VENDIDA"] = "DISPONIBLE"
    anio_creacion: int = Field(..., ge=1000, le=2026)
    artista_id: int

class ObraArteResponse(ObraArteCreate):
    id: int

# --- ESQUEMAS VENTA ---
class VentaCreate(BaseModel):
    coleccionista_id: int
    obra_id: int

class VentaResponse(BaseModel):
    id: int
    coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: datetime

# --- PAGINACIÓN ---
class PaginatedObrasResponse(BaseModel):
    items: List[ObraArteResponse]
    total: int
    pagina: int
    limite: int
    total_paginas: int