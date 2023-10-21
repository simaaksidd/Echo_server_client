# TCP/IP Server and Client Readme

## Server Specification

- Each server program listens on a socket, waits for a client to connect.
- Once connected, the server receives a message from the client, prints the message to stdout, and then waits for the next client indefinitely.
- To start a server, you provide one command-line argument: the port number to listen on for client connections.
- Servers accept and process client communications in an infinite loop, allowing multiple clients to send messages to the same server.
- Servers only exit in response to an external signal (e.g., SIGINT from pressing Ctrl-C).
- Each server maintains a short client queue, limiting it to 10 clients, and handles multiple client connection attempts concurrently via multithreaded programming.

## Client Specification

- Each client program contacts a server, reads a message from stdin, sends the message, and then exits.
- Clients read and send the message exactly as it appears in stdin until reaching an EOF (end-of-file).
- To run a client, you provide two command-line arguments: the IP address of the server and the port number of the server.
- Clients can handle arbitrarily large messages by iteratively reading and sending chunks of the message, rather than reading the whole message into memory first.
- Clients handle partial sends, where a socket only transmits part of the data given in the last send call, by attempting to re-send the rest of the data until it has all been sent.

This setup allows you to create a TCP/IP server that can accept multiple client connections, receive and process messages, and handle large or small messages efficiently and robustly. The multithreaded server architecture ensures concurrency and responsiveness.
