import socket
import threading

SERVER_IP = "0.0.0.0"
PORT = 9999

clients = {}  

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen()

    print("Server started...")

    while True:
        client_sock, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_sock,))
        thread.start()

def broadcast(message, sender_sock):
    for client in clients:
        if client != sender_sock:
            try:
                client.send(message.encode())
            except:
                client.close()

def handle_client(client_sock):
    try:
        name = client_sock.recv(1024).decode()
        clients[client_sock] = name

        print(f"{name} joined the chat")

        while True:
            msg = client_sock.recv(1024).decode()
            if not msg:
                break

            full_msg = f"{name}: {msg}"
            print(full_msg)

            broadcast(full_msg, client_sock)

    except:
        pass
    finally:
        print(f"{clients.get(client_sock,'Unknown')} left")
        clients.pop(client_sock, None)
        client_sock.close()



start_server()