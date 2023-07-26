# Data Receiver Application

The Data Receiver Application is a simple client-server application that allows you to send data from a client to a server via TCP and store the received data in files on the server.

## Requirements

- Python 3.x
- No additional Python libraries are required. All functionalities are implemented using standard Python libraries.

## Getting Started

1. Clone the repository to your local machine:
```bash
git clone https://github.com/joaohenriquedossantos/data-receiver.git
```
2. Go to the repository: 
```bash
cd data-receiver
```


3. Install Python 3 if you don't have it installed already. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

4. (Optional) Create a virtual environment to isolate the application's dependencies:
```bash
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

5. Configure the application:

   - Open the `config.ini` file and set the desired configurations for the server and client:

```ini
[SERVER]
Port = 9999              # The port on which the server will listen for incoming connections
MaxClients = 5           # The maximum number of concurrent client connections the server will accept
MaxFileSize = 1024       # The maximum size of each file in bytes (1 KB)
FilePrefix = DATA        # The prefix to be used for generated file names

[CLIENT]
Host = 127.0.0.1         # The IP address or hostname of the server
Port = 9999              # The port on which the server is listening
```
## How to Use

### Starting the Server

1. Open a terminal or command prompt.

2. Navigate to the directory where the `server.py` script and `config.ini` file are located.

3. Run the following command to start the server:

```bash
python3 server.py
```

The server will start listening for incoming connections on the configured port.

### Sending Data from the Client

1. Open a new terminal or command prompt.

2. Navigate to the directory where the client.py script and config.ini file are located.

3. Run the following command to start the client:

```bash
python3 client.py
```
The client will prompt you to enter data to send to the server:

```bash
Enter data to send to the server: <type your data here>

```

1. Type the data you want to send and press Enter.

2. The client will establish a connection to the server and send the entered data.

# Advanced Functionality

The application supports some advanced features:

1. The server can handle multiple clients simultaneously and store data from each client in separate files.
2. The server can automatically close the connection if a client does not transmit data for a configurable period.