from dataclasses import dataclass
from typing import Optional

@dataclass
class Artista:
    id: int
    nombre: str
    nacionalidad: str
    estilo_artistico: str
    obras_creadas: int = 0

@dataclass
class Coleccionista:
    id: int
    nombre: str
    correo: str
    presupuesto: float

@dataclass
class ObraArte:
    id: int
    titulo: str
    precio: float
    estado: str #disponible, reservado, vendido
    anio_creacion: int
    artista_id: int

@dataclass
class Venta:
    id: int
    Coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: str
    