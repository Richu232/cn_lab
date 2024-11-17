import socket

# Define the server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 8080          # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (max 1 connection)
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept a connection from the client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Send a "Hello" message to the client
message = "Hello, Client!"
client_socket.sendall(message.encode())  # Send encoded message

print(f"Sent message to client: {message}")

# Close the connection
client_socket.close()
server_socket.close()
