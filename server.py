import socket
import sys
def create_socket():
    try:
        global host
        global port
        global s
        host=""
        s=socket.socket()
        port=9090
    except socket.error as msg:
        print("Socket connection error"+str(msg))

def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the port")

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error")        
        bind_socket()

def accept_socket():
    conn,addr=s.accept()
    print("Connection has been established with IP",addr[0]," and port",str(addr[1]))
    send_command(conn)
    s.close()

def send_command(conn):
    while True:
        ter=input()
        if ter==0:
            conn.close()
            sys.exit()
        if len(str.encode(ter)) > 0:
            conn.send(str.encode(ter))
            client_response=str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    accept_socket()

main()