# client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1024))

while True:
    message = client.recv(1024).decode()
    print(message)

    if message == "Goodbye!":
        break

    choice = input()
    client.send(choice.encode())

    if choice == "1":
        username = input("Enter a new username: ")
        client.send(username.encode())
        password = input("Enter a new password: ")
        client.send(password.encode())
        response = client.recv(1024).decode()
        print(response)

    elif choice == "2":
        username = input("Username: ")
        client.send(username.encode())
        password = input("Password: ")
        client.send(password.encode())
        print(client.recv(1024).decode())

    elif choice == "3":
        username = input("Enter the username to delete: ")
        client.send(username.encode())
        print(client.recv(1024).decode())

client.close()