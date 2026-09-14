from typing import List, Optional, Literal
from datetime import datetime

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

class ColeccionistaCreate(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    correo: EmailStr
    presupuesto: float = Field(..., gt=0)
    es_vip: bool = False


class ColeccionistaUpdate(BaseModel):
    nombre: Optional[str] = Field(
        None,
        min_length=3,
        max_length=100
    )
    correo: Optional[EmailStr] = None
    presupuesto: Optional[float] = Field(None, gt=0)
    es_vip: Optional[bool] = None


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


class ObraArteResponse(ObraArteCreate):
    id: int


#venta

class VentaCreate(BaseModel):
    coleccionista_id: int = Field(..., gt=0)
    obra_id: int = Field(..., gt=0)


class VentaResponse(BaseModel):
    id: int
    coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: datetime


#paginacion

class PaginatedObrasResponse(BaseModel):
    items: List[ObraArteResponse]
    total: int = Field(..., ge=0)
    pagina: int = Field(..., ge=1)
    limite: int = Field(..., gt=0)
    total_paginas: int = Field(..., ge=0)