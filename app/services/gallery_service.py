from fastapi import HTTPException, status
from app.repositories.memory_repository import repo
from app.schemas.schemas import VentaCreate

#reglas de negocio

class GalleryService:
    @staticmethod
    def procesar_venta(venta_in: VentaCreate):
        coleccionista = repo.get_coleccionista_by_id(venta_in.coleccionista_id)
        if not coleccionista:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"code": "RESOURCE_NOT_FOUND", "message": f"No existe coleccionista con ID {venta_in.coleccionista_id}", "details": []}}
            )
        
        obra = repo.get_obra_by_id(venta_in.obra_id)
        if not obra:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"error": {"code": "RESOURCE_NOT_FOUND", "message": f"No existe la obra con ID {venta_in.obra_id}", "details": []}}
            )

        
        if obra["estado"] != "DISPONIBLE":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"error": {"code": "BUSINESS_RULE_VIOLATION", "message": "La obra no esta disponible para la venta", "details": []}}
            )

       
        if coleccionista["presupuesto"] < obra["precio"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"error": {"code": "INSUFFICIENT_FUNDS", "message": "El coleccionista no tiene suficiente presupuesto", "details": []}}
            )

        
        if obra["precio"] > 100000.0 and not coleccionista["es_vip"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"error": {"code": "VIP_ONLY", "message": "Obras mayores a $100,000 requieren estatus VIP", "details": []}}
            )

       
        obra["estado"] = "VENDIDA"
        coleccionista["presupuesto"] -= obra["precio"]
        return repo.registrar_venta(coleccionista["id"], obra["id"], obra["precio"])