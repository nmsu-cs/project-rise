# server.py
import sqlite3
import hashlib
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1024))
server.listen()

def handle_connection(c):
    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()

    while True:
        c.send("1. Register\n2. Login\n3. Delete User\n4. Exit\nEnter your choice: ".encode())
        choice = c.recv(1024).decode().strip()

        if choice == "1":
            c.send("Enter a new username: ".encode())
            username = c.recv(1024).decode().strip()
            c.send("Enter a new password: ".encode())
            password = hashlib.sha256(c.recv(1024)).hexdigest()

            try:
                cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                c.send("Registration successful!\n".encode())
            except sqlite3.IntegrityError:
                c.send("Username already exists. Please try again.\n".encode())

        elif choice == "2":
            c.send("Username: ".encode())
            username = c.recv(1024).decode().strip()
            c.send("Password: ".encode())
            password = hashlib.sha256(c.recv(1024)).hexdigest()

            cursor.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
            if cursor.fetchall():
                c.send("Login Successful\n".encode())
            else:
                c.send("Login Failed\n".encode())

        elif choice == "3":
            c.send("Enter the username to delete: ".encode())
            username = c.recv(1024).decode().strip()

            cursor.execute("DELETE FROM userdata WHERE username = ?", (username,))
            if cursor.rowcount > 0:
                conn.commit()
                c.send(f"User '{username}' deleted successfully.\n".encode())
            else:
                c.send(f"User '{username}' not found.\n".encode())

        elif choice == "4":
            c.send("Goodbye!".encode())
            c.close()
            break

        else:
            c.send("Invalid choice. Please try again.\n".encode())

    conn.close()

while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()