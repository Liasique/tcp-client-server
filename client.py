import socket

HOST = '127.0.0.1'  # має збігатися з сервером
PORT = 12345        # той самий порт, що і в server.py

# Створюємо TCP-сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Підключення до сервера
    s.sendall("Привіт від клієнта!".encode('utf-8'))  # Надсилаємо повідомлення
    data = s.recv(1024)  # Отримуємо відповідь

print("Отримано від сервера:", data.decode('utf-8'))