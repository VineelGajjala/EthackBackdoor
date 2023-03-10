# PASSWORD IS hill lowercase

import sys
import socket

SEND_BUFFER_SIZE = 2048
RECV_BUFFER_SIZE = 2048

def client(server_ip, ports):
    i = 0
    server_port = ports[i]
    # server_port = 443
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            try:
                s.connect((server_ip, server_port))
            except:
                i += 1
                if i >= len(ports):
                    print("Failed to connect")
                    return
                server_port = ports[i]
            else:
                break

        guesses = 0
        while True:
            guesses += 1
            if guesses >= 4:
                print("Failed verification, connection closing")
                s.close()
                return
            password = input("Enter password: ") #password to type
            s.sendall(password.encode('utf-8')) #send password
            passwordValidation = s.recv(RECV_BUFFER_SIZE).decode('utf-8') == "SUCCESS" # receive verification on pass
            if passwordValidation:
                break
            else:
                print("Incorrect verification... Try again")



        print("Welcome to the machine")
        while True:
            cmd = input("[root@week4 /]# ")
            if (cmd == "exit"):
                print("You've exited")
                break
            s.sendall(cmd.encode('utf-8'))
            data = s.recv(RECV_BUFFER_SIZE)
            print(data.decode('utf-8'))

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python client-python.py [Server IP]")
    server_ip = sys.argv[1]
    ports = [4000, 4001, 4002, 4003, 4004, 4005,4006,4007,4008,4009, 4010]
    client(server_ip, ports)

if __name__ == "__main__":
    main()