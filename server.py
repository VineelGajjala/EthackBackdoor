import sys
import socket
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def handle_req(conn, addr):
    with conn:
        while True:
            data = conn.recv(RECV_BUFFER_SIZE)
            if not data: break
            print(data.decode('utf-8'), end='')

def server(server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', server_port))
        s.listen(QUEUE_LENGTH)
        while True:
            conn, addr = s.accept()
            print("did we accept?") # we accept here
            worker_thread = threading.Thread(target=handle_req, args=(conn, addr,))
            worker_thread.start()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    print("hi")
    main()