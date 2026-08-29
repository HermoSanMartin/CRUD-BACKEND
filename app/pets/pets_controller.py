from fastapi import APIRouter
from app.shared.response_builder import build_response
from app import pets

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service

router = APIRouter(
    prefix="/api/students/{studentId}/pets",
    tags=["Pets"],
)


@router.get("")
def find_all(studentId: str):
    pets=pets_service.find_all_for_student(studentId)
    return build_response(
        success=True,
        status_code=200,
        message="Lista de mascotas",
        data=pets
    )


@router.post("", status_code=201)
def create(studentId: str, body: CreatePetDto):
    created_pets=pets_service.create(studentId, body)
    return build_response(
        success=True,
        status_code=201,
        message="mascota creada",
        data=created_pets
    )


@router.patch("/{petId}")
def update(studentId: str, petId: str, body: UpdatePetDto):
    update_pets=pets_service.update(studentId, petId, body)
    return build_response(
        success=True,
        status_code=200,
        message="mascota actualizada",
        data=update_pets
    )


@router.delete("/{petId}")
def delete(studentId: str, petId: str):
    deleted=pets_service.delete(studentId, petId)
    return build_response(
        success=True,
        status_code=200,
        message="mascota borrada correctamente",
        data=deleted
    )
