from fastapi import HTTPException, status

class ColeccionistaService:
    def __init__(self, repository, pet_repository=None):
        self.repository = repository
        self.pet_repository = pet_repository

    def crear_coleccionista(self, data):
        # RBN-01: Edad Mínima (>= 18 años)
        if data.edad < 18:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"code": "UNDERAGE_USER", "message": "El coleccionista debe ser mayor de 18 años"}
            )
        
        # RBN-02: Unicidad de Correo
        existente = self.repository.obtener_por_email(data.email)
        if existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "EMAIL_ALREADY_EXISTS", "message": "El correo electronico ya esta registrado"}
            )
            
        return self.repository.crear(data)

    def eliminar_coleccionista(self, id: int):
        # RBN-03: Integridad Relacional (Impedir borrado si tiene mascotas)
        if self.pet_repository:
            mascotas = self.pet_repository.obtener_por_dueno(id)
            if len(mascotas) > 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail={"code": "HAS_DEPENDENCIES", "message": "No se puede eliminar un coleccionista que tiene mascotas asociadas"}
                )
        
        exito = self.repository.eliminar(id)
        if not exito:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "RESOURCE_NOT_FOUND", "message": f"No existe el coleccionista con ID {id}"}
            )
        return True