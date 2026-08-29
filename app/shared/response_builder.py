from typing import Any


def build_response(success: bool, status_code: int, message: str, data: Any = None) -> dict:
    return {
        "success": success,
        "status_code": status_code,
        "message": message,
        "data": data
    }