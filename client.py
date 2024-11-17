import socket

# Define the server address and port
HOST = '127.0.0.1'  # Localhost
PORT = 8080          # Port to connect to

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive the message from the server
message = client_socket.recv(1024).decode()  # Receive and decode the message
print(f"Received from server: {message}")

# Close the socket
client_socket.close()
