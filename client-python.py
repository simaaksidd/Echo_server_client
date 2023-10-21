###############################################################################
# client-python.py
# Name: Simaak Siddiqi
# EID: srs5826
###############################################################################
import sys
import socket

SEND_BUFFER_SIZE = 2048
FORMAT = 'utf-8'
MESSAGE = sys.stdin.read()
def client(server_ip, server_port):

    def send(msg):
        while msg:
            chunk = msg[:SEND_BUFFER_SIZE]
            msg = msg[SEND_BUFFER_SIZE:]
            chunk = chunk.encode(FORMAT)
            chunk_length = len(chunk)
            sendl = str(chunk_length).encode(FORMAT)
            sendl += b' ' * ( SEND_BUFFER_SIZE - len(sendl)) 
            client.send(sendl)
            client.send(chunk)
            client.close()
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    send(MESSAGE)

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
