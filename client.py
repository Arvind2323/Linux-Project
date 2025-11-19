import socket

def send_request(message, host="127.0.0.1", port=5000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()

    client_socket.close()
    return response

if __name__ == "__main__":
    while True:
        req = input("Enter operation (e.g., add 5 3) or 'quit': ")

        if req == "quit":
            break

        result = send_request(req)
        print("Result:", result)
