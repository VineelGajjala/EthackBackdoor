import sys
import socket

SEND_BUFFER_SIZE = 2048
RECV_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        while True:
            print(s.recv(RECV_BUFFER_SIZE).decode('utf-8'))
            password = input()
            s.sendall()

        print("Welcome to the machine")
        while True:
            x = input("[root@week4 /]# ")
            if (x == "exit"):
                print("You've exited")
                break
            s.sendall(x.encode('utf-8'))
            data = s.recv(RECV_BUFFER_SIZE)
            print(data.decode('utf-8'))

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()