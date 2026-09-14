from fastapi import APIRouter, HTTPException, Query, status
from typing import Optional, Literal
from app.schemas.schemas import ObraArteCreate, ObraArteResponse, PaginatedObrasResponse
from app.repositories.memory_repository import repo

router = APIRouter(prefix="/obras", tags=["Obras de Arte"])

@router.post("", response_model=ObraArteResponse, status_code=status.HTTP_201_CREATED)
def crear_obra(obra: ObraArteCreate):
    artista = repo.get_artista_by_id(obra.artista_id)
    if not artista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "RELATED_RESOURCE_NOT_FOUND", "message": f"El artista con ID {obra.artista_id} no existe", "details": []}}
        )
    return repo.create_obra(obra.model_dump())

@router.get("", response_model=PaginatedObrasResponse, status_code=status.HTTP_200_OK)
def listar_obras(
    estado: Optional[Literal["DISPONIBLE", "RESERVADA", "VENDIDA"]] = Query(None, description="Filtro por estado"),
    ordenar_por: str = Query("precio", description="Atributo para ordenar (precio, anio_creacion, id)"),
    direccion: Literal["asc", "desc"] = Query("asc", description="Direccion: asc o desc"),
    pagina: int = Query(1, ge=1, description="Numero de pagina"),
    limite: int = Query(10, ge=1, le=100, description="Elementos por pagina")
):
    items = repo.get_all_obras()

    # filtrado
    if estado:
        items = [o for o in items if o["estado"] == estado]

    
    reverse = (direccion == "desc")
    if ordenar_por in ["precio", "anio_creacion", "id"]:
        items = sorted(items, key=lambda x: x.get(ordenar_por, 0), reverse=reverse)

    #pag
    total = len(items)
    inicio = (pagina - 1) * limite
    fin = inicio + limite
    elementos_paginados = items[inicio:fin]
    total_paginas = (total + limite - 1) // limite if total > 0 else 1

    return {
        "items": elementos_paginados,
        "total": total,
        "pagina": pagina,
        "limite": limite,
        "total_paginas": total_paginas
    }

@router.get("/{obra_id}", response_model=ObraArteResponse, status_code=status.HTTP_200_OK)
def obtener_obra(obra_id: int):
    obra = repo.get_obra_by_id(obra_id)
    if not obra:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "RESOURCE_NOT_FOUND", "message": f"No existe la obra con ID {obra_id}", "details": []}}
        )
    return obra