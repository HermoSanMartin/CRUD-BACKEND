from typing import List, Optional
from datetime import datetime

class MemoryRepository:
    def __init__(self):
        self.artistas: List[dict] = [
            {"id": 1, "nombre": "Vincent van Gogh", "nacionalidad": "Holandesa", "estilo_principal": "Postimpresionismo", "obras_creadas": 12},
            {"id": 2, "nombre": "Claude Monet", "nacionalidad": "Francesa", "estilo_principal": "Impresionismo", "obras_creadas": 8}
        ]
        self.coleccionistas: List[dict] = [
            {"id": 1, "nombre": "Sebastian", "correo": "sebastian@example.com", "presupuesto": 500000.0, "es_vip": True},
            {"id": 2, "nombre": "Mateo", "correo": "mateo@example.com", "presupuesto": 5000.0, "es_vip": False}
        ]
        self.obras: List[dict] = [
            {"id": 1, "titulo": "La Noche Estrellada", "precio": 150000.0, "estado": "DISPONIBLE", "anio_creacion": 1889, "artista_id": 1},
            {"id": 2, "titulo": "Los Girasoles", "precio": 90000.0, "estado": "DISPONIBLE", "anio_creacion": 1888, "artista_id": 1},
            {"id": 3, "titulo": "Impression, Soleil Levant", "precio": 120000.0, "estado": "DISPONIBLE", "anio_creacion": 1872, "artista_id": 2}
        ]
        self.ventas: List[dict] = []
        
        self._next_col_id = 3
        self._next_obra_id = 4
        self._next_venta_id = 1

    # Artistas
    def get_all_artistas(self) -> List[dict]: return self.artistas
    def get_artista_by_id(self, art_id: int) -> Optional[dict]:
        return next((a for a in self.artistas if a["id"] == art_id), None)

    # Coleccionistas
    def create_coleccionista(self, data: dict) -> dict:
        data["id"] = self._next_col_id
        self._next_col_id += 1
        self.coleccionistas.append(data)
        return data

    def get_coleccionista_by_id(self, col_id: int) -> Optional[dict]:
        return next((c for c in self.coleccionistas if c["id"] == col_id), None)

    def get_all_coleccionistas(self) -> List[dict]: return self.coleccionistas

    def update_coleccionista(self, col_id: int, update_data: dict) -> Optional[dict]:
        col = self.get_coleccionista_by_id(col_id)
        if not col: return None
        for k, v in update_data.items():
            if v is not None: col[k] = v
        return col

    def delete_coleccionista(self, col_id: int) -> bool:
        col = self.get_coleccionista_by_id(col_id)
        if col:
            self.coleccionistas.remove(col)
            return True
        return False

    # Obras
    def create_obra(self, data: dict) -> dict:
        data["id"] = self._next_obra_id
        self._next_obra_id += 1
        self.obras.append(data)
        return data

    def get_obra_by_id(self, obra_id: int) -> Optional[dict]:
        return next((o for o in self.obras if o["id"] == obra_id), None)

    def get_all_obras(self) -> List[dict]: return self.obras

    # Ventas
    def registrar_venta(self, coleccionista_id: int, obra_id: int, monto: float) -> dict:
        venta = {
            "id": self._next_venta_id,
            "coleccionista_id": coleccionista_id,
            "obra_id": obra_id,
            "monto_total": monto,
            "fecha": datetime.now() 
        }
        self._next_venta_id += 1
        self.ventas.append(venta) 
        return venta


repo = MemoryRepository()