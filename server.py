from __future__ import annotations

import socket
from typing import Callable

from .marshalling import marshal_response, unmarshal_request
from .models import StudentProfile


def calculate_grade_average(profile: StudentProfile) -> float:
    if not profile.grades:
        return 0.0
    return sum(profile.grades) / len(profile.grades)


class RPCServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 5000) -> None:
        self.host = host
        self.port = port
        self.methods: dict[str, Callable[[StudentProfile], float]] = {
            "calculate_grade_average": calculate_grade_average,
        }

    def serve_once(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            connection, _ = server_socket.accept()
            with connection:
                raw_request = self._read_line(connection)
                try:
                    method_name, profile = unmarshal_request(raw_request)
                    if method_name not in self.methods:
                        raise ValueError(f"Unknown method: {method_name}")
                    result = self.methods[method_name](profile)
                    connection.sendall(marshal_response(result=result))
                except (TypeError, ValueError) as exc:
                    connection.sendall(marshal_response(error=str(exc)))

    @staticmethod
    def _read_line(connection: socket.socket) -> bytes:
        chunks = []
        while True:
            chunk = connection.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
            if b"\n" in chunk:
                break
        return b"".join(chunks).strip()


if __name__ == "__main__":
    RPCServer().serve_once()
