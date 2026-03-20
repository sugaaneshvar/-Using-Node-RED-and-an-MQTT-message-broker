from __future__ import annotations

from typing import Any

from .models import StudentProfile


def validate_types(data: Any, schema: Any, path: str = "payload") -> None:
    """Validate incoming JSON-like data against a lightweight schema."""
    if isinstance(schema, dict):
        if not isinstance(data, dict):
            raise TypeError(f"{path} expected dict, got {type(data).__name__}")
        for key, child_schema in schema.items():
            if key not in data:
                raise TypeError(f"{path}.{key} is required")
            validate_types(data[key], child_schema, f"{path}.{key}")
        return

    if isinstance(schema, list):
        if len(schema) != 1:
            raise ValueError("List schemas must contain exactly one item type")
        if not isinstance(data, list):
            raise TypeError(f"{path} expected list, got {type(data).__name__}")
        for index, value in enumerate(data):
            validate_types(value, schema[0], f"{path}[{index}]")
        return

    if not isinstance(data, schema):
        raise TypeError(f"{path} expected {schema.__name__}, got {type(data).__name__}")


STUDENT_PROFILE_SCHEMA = {
    "name": str,
    "id": int,
    "grades": [int],
}


def marshal_request(method: str, params: dict[str, Any]) -> bytes:
    import json

    body = {"method": method, "params": params}
    return (json.dumps(body) + "\n").encode("utf-8")


def unmarshal_request(raw_message: bytes) -> tuple[str, StudentProfile]:
    import json

    message = json.loads(raw_message.decode("utf-8"))
    validate_types(message, {"method": str, "params": STUDENT_PROFILE_SCHEMA})
    method = message["method"]
    params = message["params"]
    profile = StudentProfile(
        name=params["name"],
        id=params["id"],
        grades=params["grades"],
    )
    return method, profile


def marshal_response(result: Any = None, error: str | None = None) -> bytes:
    import json

    body = {"result": result, "error": error}
    return (json.dumps(body) + "\n").encode("utf-8")


def unmarshal_response(raw_message: bytes) -> dict[str, Any]:
    import json

    return json.loads(raw_message.decode("utf-8"))
