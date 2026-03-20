from __future__ import annotations

import socket

from .marshalling import marshal_request, unmarshal_response
from .models import StudentProfile


class RPCClient:
    def __init__(self, host: str = "127.0.0.1", port: int = 5000) -> None:
        self.host = host
        self.port = port

    def calculate_grade_average(self, profile: StudentProfile) -> float:
        payload = {
            "name": profile.name,
            "id": profile.id,
            "grades": profile.grades,
        }
        response = self._send_request("calculate_grade_average", payload)
        if response["error"]:
            raise TypeError(response["error"])
        return float(response["result"])

    def _send_request(self, method: str, params: dict) -> dict:
        with socket.create_connection((self.host, self.port)) as client_socket:
            client_socket.sendall(marshal_request(method, params))
            raw_response = self._read_line(client_socket)
        return unmarshal_response(raw_response)

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
