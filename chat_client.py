import socket
import threading

SERVER_IP = "127.0.0.1"
PORT = 9999

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            print(message)
        except:
            print("Disconnected from server")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    name = input("Enter your name: ")
    client.send(name.encode()) 

    print("WELCOME TO THE CHAT ROOM")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        client.send(msg.encode())

start_client()