import socket, threading, time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 22222))
server_socket.listen(10)
print("Server listen")

encoding = "utf-8"

counter = 0
start_time = time.time()
while time.time() < start_time + 1000 * 15:
    
    client_socket, client_address = server_socket.accept()
    
    data = client_socket.recv(1024).decode(encoding)
    print(data)
    client_socket.sendall(data.encode(encoding))
    
    client_socket.close()

server_socket.close()
