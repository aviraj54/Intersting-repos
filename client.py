import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8080))

print("Connected to server!")
data = client.recv(1024)
client.send(b"i m client")

print(data.decode())