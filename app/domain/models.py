from dataclasses import dataclass

@dataclass
class Artista:
    id: int
    nombre: str
    nacionalidad: str
    estilo_principal: str
    obras_creadas: int = 0

@dataclass
class Coleccionista:
    id: int
    nombre: str
    correo: str
    presupuesto: float
    es_vip: bool = False

@dataclass
class ObraArte:
    id: int
    titulo: str
    precio: float
    estado: str  # DISPONIBLE, RESERVADA, VENDIDA
    anio_creacion: int
    artista_id: int

@dataclass
class Venta:
    id: int
    coleccionista_id: int
    obra_id: int
    monto_total: float
    fecha: str