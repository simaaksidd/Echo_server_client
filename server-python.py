###############################################################################
# server-python.py
# Name: Simaak Siddiqi
# EID: srs5826
###############################################################################
import sys
import socket
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10
FORMAT = 'utf-8'
OUTPUT_FILE = 'out.txt'


def server(server_port):
        # handle client
    def handle_client(conn, addr):
        print(f"[NEW CONNECTION] {addr} has connected.")
        while True:
            msg_length = conn.recv(RECV_BUFFER_SIZE).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                print(f'[{addr}] {msg}')
                with open(OUTPUT_FILE, 'w') as out_file:
                    out_file.write(msg)
    
    def start(host):
        print(f'[LISTENING] Server is listening on {host}')
        s.listen()
        while True:
            # When the connection is accepted, the client and server negotiate a new socket
            # the new socket, conn, will interact with the address return, addr, which contains the the port the socket will use.
            conn, addr = s.accept()
            #add multiple threads
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    
    # SET UP THE LISTENING SOCKET
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = server_port
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("[STARTING] Server is starting...")
    start(HOST)
     
    pass

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    ...
    main()
