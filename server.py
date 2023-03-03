import sys
import socket
import threading
import os
import subprocess

RECV_BUFFER_SIZE = 2048
SEND_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def handle_req(conn, addr):
    with conn:
        while True:
            data = conn.recv(RECV_BUFFER_SIZE)
            if not data: break
            output = os.popen(data.decode('utf-8')).read()
            if len(output) == 0:
                conn.sendall("No output given from command".encode('utf-8'))
            else:    
                conn.sendall(output.encode('utf-8'))
            # print("did we send the data?") Data sends correctly
            

def server(server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', server_port))
        s.listen(QUEUE_LENGTH)
        hashedCorrect = 123
        flag = False
        while True:
            conn, addr = s.accept()
            print('Connection accepted')
            for i in range(3):
                conn.sendall('Enter password: '.encode('utf-8'))
                data = conn.recv(RECV_BUFFER_SIZE)
                hashedData = data #with hashing
                if hashedData == hashedCorrect:
                    flag = True
                    break
            if not flag:
                conn.sendall("Incorrect".encode('utf-8'))
                conn.close()
                continue
                
            worker_thread = threading.Thread(target=handle_req, args=(conn, addr,))
            worker_thread.start()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()