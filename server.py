import socket

HOST = '127.0.0.1'  # localhost
PORT = 12345        # Порт має збігатися з client.py

# Створюємо TCP-сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Прив'язуємо до адреси і порту
server_socket.bind((HOST, PORT))

# Слухаємо максимум 1 підключення
server_socket.listen(1)

print("Сервер запущено. Очікуємо на з'єднання...")

# Приймаємо підключення
conn, addr = server_socket.accept()
print(f"Підключено клієнта: {addr}")

# Отримуємо байти
data = conn.recv(1024)
print("Отримано байти:", data)
print("Декодовано:", data.decode('utf-8'))

# Відправляємо відповідь
response = "Сервер каже: Привіт, клієнте!".encode('utf-8')
conn.sendall(response)

# Закриваємо з'єднання
conn.close()
server_socket.close()
print("Сервер завершив роботу.")