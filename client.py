import socket
import configparser

# read the settings
config = configparser.ConfigParser()
config.read('config.ini')

# client settings
HOST = config['CLIENT']['Host']
PORT = int(config['CLIENT']['Port'])

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Get user input
    data_to_send = input("Enter data to send to the server: ")

    # Send data to server
    client_socket.send(data_to_send.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
