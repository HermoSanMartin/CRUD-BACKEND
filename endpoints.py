
@app.get("/usuarios/{id}")
def get_user(id: int):
    return {"id": id, "nombre": "Juan"}


@app.get("/usuarios/{id}", response_model=ApiResponse[dict])
def get_user(id: int):
   
    user_data = {"id": id, "nombre": "Juan"}
    
    return ApiResponse(
        success=True,
        message="Usuario obtenido correctamente",
        data=user_data,
        errors=None
    )