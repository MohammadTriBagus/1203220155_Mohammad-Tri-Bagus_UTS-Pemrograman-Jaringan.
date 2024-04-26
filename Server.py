import socket
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
BUFFER_SIZE = 1024
COLORS = ["white", "gray", "gold", "red", "green", "blue", "yellow", "pink", "purple", "brown", "black"]

def generate_random_color():
    return random.choice(COLORS)

def handle_client_request(server_socket, client_address):
    color = generate_random_color()
    server_socket.sendto(color.encode("utf-8"), client_address)
    print(f"Sent color {color} to {client_address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))

    print(f"Server running on {SERVER_IP}:{SERVER_PORT}")

    try:
        while True:
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            data = data.decode("utf-8")

            if data == "request_color":
                handle_client_request(server_socket, client_address)

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()