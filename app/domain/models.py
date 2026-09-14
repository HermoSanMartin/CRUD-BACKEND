from dataclasses import dataclass
lienlafelipe
from typing import Optional
main

@dataclass
class Artista:
    id: int
    nombre: str
    nacionalidad: str
lienlafelipe
    estilo_principal: str
    estilo_artistico: str
main
    obras_creadas: int = 0

@dataclass
class Coleccionista:
    id: int
    nombre: str
    correo: str
    presupuesto: float
lienlafelipe
    es_vip: bool = False
main

@dataclass
class ObraArte:
    id: int
    titulo: str
    precio: float
lienlafelipe
    estado: str  # DISPONIBLE, RESERVADA, VENDIDA
    estado: str #disponible, reservado, vendido
main
    anio_creacion: int
    artista_id: int

@dataclass
class Venta:
    id: int
lienlafelipe
    coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: str
    Coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: str
    
main
