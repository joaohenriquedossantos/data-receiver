import socket
import configparser
import threading
from datetime import datetime

# read the settings
config = configparser.ConfigParser()
config.read('config.ini')

# server settings
HOST = '0.0.0.0'
PORT = int(config['SERVER']['Port'])
MAX_CLIENTS = int(config['SERVER']['MaxClients'])
MAX_FILE_SIZE = int(config['SERVER']['MaxFileSize'])
FILE_PREFIX = config['SERVER']['FilePrefix']

def handle_client(client_socket):
    # Receive customer data and save to file
    file_name = f"{FILE_PREFIX}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    current_file_size = 0

    with open(file_name, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            current_file_size += len(data)
            if current_file_size > MAX_FILE_SIZE:
                break

            f.write(data)

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX_CLIENTS)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
