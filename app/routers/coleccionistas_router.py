from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.schemas import ColeccionistaCreate, ColeccionistaUpdate, ColeccionistaResponse
from app.repositories.memory_repository import repo

router = APIRouter(prefix="/coleccionistas", tags=["Coleccionistas"])

@router.post("", response_model=ColeccionistaResponse, status_code=status.HTTP_201_CREATED)
def crear_coleccionista(coleccionista: ColeccionistaCreate):
    return repo.create_coleccionista(coleccionista.model_dump())

@router.get("", response_model=List[ColeccionistaResponse], status_code=status.HTTP_200_OK)
def listar_coleccionistas():
    return repo.get_all_coleccionistas()

@router.get("/{col_id}", response_model=ColeccionistaResponse, status_code=status.HTTP_200_OK)
def obtener_coleccionista(col_id: int):
    col = repo.get_coleccionista_by_id(col_id)
    if not col:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "RESOURCE_NOT_FOUND", "message": f"No existe coleccionista con ID {col_id}", "details": []}}
        )
    return col

@router.put("/{col_id}", response_model=ColeccionistaResponse, status_code=status.HTTP_200_OK)
def actualizar_coleccionista(col_id: int, update_data: ColeccionistaUpdate):
    updated = repo.update_coleccionista(col_id, update_data.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "RESOURCE_NOT_FOUND", "message": f"No existe coleccionista con ID {col_id}", "details": []}}
        )
    return updated

@router.delete("/{col_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_coleccionista(col_id: int):
    success = repo.delete_coleccionista(col_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "RESOURCE_NOT_FOUND", "message": f"No existe coleccionista con ID {col_id}", "details": []}}
        )
    return None