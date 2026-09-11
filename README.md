# backend-2026-grupo-XX - API REST con FastAPI

API REST funcional desarrollada con **FastAPI**, **Pydantic** y **Uvicorn** para la gestión integral de Coleccionistas y la administración de sus entidades asociadas. El proyecto implementa persistencia en memoria (listas y diccionarios), arquitectura multicapa con separación estricta de responsabilidades, validación de datos de entrada y un formato unificado para la gestión de errores.

---

## 1. Integrantes y Áreas de Responsabilidad

De acuerdo con la organización obligatoria del proyecto backend, las responsabilidades del equipo están distribuidas de la siguiente manera:

| Integrante | Área de Responsabilidad Principal | Tareas Clave |
| :--- | :--- | :--- |
| **Felipe Lienlaf** | Lógica de Negocio y Configuración | Configuración de entorno virtual, dependencias, integración de servicios y reglas del negocio. |
| **Sebastián San Martín** | Dominio, Modelos y Repositorios | Diseñar entidades del dominio, tipos de datos, repositorios en memoria y DTOs con Pydantic. |
| **[Nombre Integrante 3]** | API, Routers y Contrato REST | Implementación de endpoints, manejo de query/path parameters, respuestas HTTP y ruteo. |
| **[Nombre Integrante 4]** | Calidad, Pruebas y Documentación | Colección de pruebas en Postman/Thunder Client, validación de casos de error y redacción del README. |

---

## 2. Definición del Problema y Alcance (P1 - P7)

### P1. Situación Concreta Actual
Actualmente, los coleccionistas de ítems y mascotas registran su inventario, intercambios y datos personales mediante planillas de cálculo separadas o notas manuales. Esto genera inconsistencias en la información, imposibilidad de consultar disponibilidad en tiempo real y errores al intentar asociar mascotas o colecciones a un usuario.

### P2. Actores del Sistema
1. **Administrador del Sistema:** Encargado de registrar, actualizar, consultar y dar de baja coleccionistas y recursos asociados.
2. **Coleccionista / Usuario:** Consulta su catálogo, gestiona sus colecciones y verifica el estado de sus registros.

### P3. Consecuencias del Problema
* **Pérdida de Trazabilidad:** Incapacidad de rastrear a quién pertenece cada ítem o mascota de manera precisa.
* **Duplicidad de Datos:** Creación de registros repetidos con correos o IDs inconsistentes debido a la falta de validaciones de entrada.

### P4. Información Administrada por el Backend
El backend permite registrar, consultar, modificar y eliminar la información de:
* **Coleccionistas:** ID, nombre, correo electrónico, edad, estado activo/inactivo.
* **Mascotas (`pets`):** ID, nombre, especie, edad, ID del coleccionista dueño.
* **Estudiantes (`students`):** ID, nombre, carrera, nivel.
* **Galería (`gallery_service`):** Relaciones de exhibición de colecciones.

### P5. Acciones Permitidas (Requisitos Funcionales)
1. El sistema debe permitir registrar un nuevo coleccionista con validación de correo y edad.
2. El sistema debe permitir consultar el listado completo de coleccionistas con soporte de paginación, filtro y orden.
3. El sistema debe permitir obtener los detalles de un coleccionista específico mediante su ID.
4. El sistema debe permitir actualizar la información parcial o total de un coleccionista existente.
5. El sistema debe permitir eliminar un coleccionista del registro en memoria.
6. El sistema debe permitir registrar mascotas asociadas a un coleccionista existente.
7. El sistema debe permitir listar todas las mascotas y filtrarlas por su identificador.
8. El sistema debe permitir registrar y consultar estudiantes en el módulo auxiliar.

### P6. Exclusiones del Alcance (Lo que NO resuelve esta versión)
1. **Sin Interfaz Gráfica (Frontend):** Se expone únicamente la API REST funcional.
2. **Sin Persistencia en Base de Datos:** Los datos residen temporalmente en memoria (al reiniciar el servidor se restablecen).
3. **Sin Autenticación ni Autorización:** No incluye JWT, OAuth2 ni gestión de sesiones/contraseñas.

### P7. Criterios de Aceptación
1. El comando `uvicorn app.main:app --reload` inicia el servidor local sin errores.
2. El endpoint `GET /coleccionistas` ejecuta correctamente la secuencia: **1° Filtrar -> 2° Ordenar -> 3° Paginar**.
3. Todos los errores controlados devuelven una estructura JSON uniforme con código, mensaje y detalles[cite: 2].
4. Los endpoints devuelven códigos HTTP semánticamente correctos (`200`, `201`, `204`, `400`, `404`, `422`)[cite: 2].
5. La documentación Swagger en `/docs` permite probar el 100% de los endpoints[cite: 2].

---

## 3. Modelo del Dominio y Reglas de Negocio

### Diagrama de Clases (Representación)
```text
 +-------------------+         1 : N         +-------------------+
 |   Coleccionista   | --------------------< |       Pet         |
 +-------------------+                       +-------------------+
 | - id: int         |                       | - id: int         |
 | - nombre: str     |                       | - nombre: str     |
 | - email: EmailStr |                       | - especie: str    |
 | - edad: int       |                       | - edad: int       |
 | - activo: bool    |                       | - owner_id: int   |
 +-------------------+                       +-------------------+

 +-------------------+                       +-------------------+
 |     Student       |                       |  GalleryService   |
 +-------------------+                       +-------------------+
 | - id: int         |                       | - id: int         |
 | - nombre: str     |                       | - titulo: str     |
 | - carrera: str    |                       | - coleccion_id:int|
 +-------------------+                       +-------------------+