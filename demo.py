from __future__ import annotations

import json
import socket
import threading
import time

from rpc_marshalling_url.client import RPCClient
from rpc_marshalling_url.models import StudentProfile
from rpc_marshalling_url.server import RPCServer


def run_server_once(port: int) -> threading.Thread:
    server = RPCServer(port=port)
    thread = threading.Thread(target=server.serve_once, daemon=True)
    thread.start()
    time.sleep(0.2)
    return thread


def send_invalid_payload(port: int) -> dict:
    invalid_payload = {
        "method": "calculate_grade_average",
        "params": {
            "name": "Asha",
            "id": "21",
            "grades": [90, 80, 70],
        },
    }
    with socket.create_connection(("127.0.0.1", port)) as client_socket:
        client_socket.sendall((json.dumps(invalid_payload) + "\n").encode("utf-8"))
        raw_response = client_socket.recv(4096).decode("utf-8").strip()
    return json.loads(raw_response)


def main() -> None:
    valid_port = 5050
    valid_server = run_server_once(valid_port)
    client = RPCClient(port=valid_port)
    profile = StudentProfile(name="Asha", id=21, grades=[90, 80, 70, 100])
    average = client.calculate_grade_average(profile)
    print(f"Valid RPC result: {average:.2f}")
    valid_server.join(timeout=1)

    invalid_port = 5051
    invalid_server = run_server_once(invalid_port)
    invalid_response = send_invalid_payload(invalid_port)
    print(f"Invalid RPC response: {invalid_response['error']}")
    invalid_server.join(timeout=1)


if __name__ == "__main__":
    main()
