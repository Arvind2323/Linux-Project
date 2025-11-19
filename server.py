import socket

def perform_operation(request):
    parts = request.strip().split()

    if len(parts) != 3:
        return "ERROR: Invalid format. Use: operation num1 num2"

    operation, a, b = parts
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "ERROR: Arguments must be numbers."

    if operation == "add":
        return str(a + b)
    elif operation == "subtract":
        return str(a - b)
    elif operation == "multiply":
        return str(a * b)
    elif operation == "divide":
        if b == 0:
            return "ERROR: Division by zero."
        return str(a / b)
    else:
        return "ERROR: Unknown operation."

def start_server(host="127.0.0.1", port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"RPC Math Server running on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr}")

        request = client_socket.recv(1024).decode()
        print(f"Received: {request}")

        response = perform_operation(request)
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
