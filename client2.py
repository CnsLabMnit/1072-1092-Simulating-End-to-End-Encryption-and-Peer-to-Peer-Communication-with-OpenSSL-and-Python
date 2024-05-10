import socket

def chat_with_ip2():
    host = '172.22.58.252'  # Replace 'ip2' with the actual IP address of the second system
    port = 50000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("You: ")
        client_socket.send(message.encode())

        if message.lower() == 'exit':
            break

        received_message = client_socket.recv(1024).decode()
        print(f"IP2: {received_message}")

    client_socket.close()

if __name__ == "_main_":
   chat_with_ip2()