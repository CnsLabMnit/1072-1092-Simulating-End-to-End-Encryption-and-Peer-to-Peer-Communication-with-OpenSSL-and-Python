import socket

def chat_with_ip1():
    host = '172.22.58.252'  # Replace 'ip1' with the actual IP address of the first system
    port = 50000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Waiting for connection...")
    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        received_message = client_socket.recv(1024).decode()
        print(f"IP1: {received_message}")

        if received_message.lower() == 'exit':
            break

        message = input("You: ")
        client_socket.send(message.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "_main_":
   chat_with_ip1()