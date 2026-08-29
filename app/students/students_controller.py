from fastapi import APIRouter
from app import students
from app.pets.pets_service import pets_service
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service
from app.shared.response_builder import build_response

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all():
    students=students_service.find_all()
    return build_response(
        success=True,
        status_code=200,
        message="lista de estudiantes",
        data=students
    )


@router.get("/{student_id}")
def find_by_id(student_id: str):
    student=students_service.find_by_id(student_id)
    return build_response(
        success=True,
        status_code=200,
        message="estudiante encontrado",
        data=student


    )


@router.post("", status_code=201)
def create(body: CreateStudentDto):
    created_student=students_service.create(body)
    return build_response(
        success=True,
        status_code=201,
        message="estudiante creado",
        data=created_student
    )


@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto):
    update_student=students_service.update(student_id, body)
    return build_response(
        success=True,
        status_code=200,
        message="estudiante actulizado",
        data=update_student

    )


@router.delete("/{student_id}")
def delete(student_id: str):
    deleted = students_service.delete(student_id)
    pets_service.delete_all_for_student(student_id)
    return build_response(
        success=True,
        status_code=200,
        message="estudiante y mascota eliminados correctamente",
        data=deleted
    )
