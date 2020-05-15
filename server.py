import socket
import threading
import sys






def newClient(clientsocket,address):
    print(SV_THREAD)
    print(SV_CONNECTION,address)
    while True:
        msg = "Testing architecture"
        clientsocket.send(msg.encode())
        clientmsg = clientsocket.recv(1024)
        print(clientmsg.decode())


if __name__ == "__main__":

    SV_START = "Server starting...\n"
    SV_WAITING = "Server waiting for clients \n"
    SV_CONNECTION = "Server got connection from"
    SV_THREAD = "Initializing thread.."
    SCKT_ERROR = "Error while creating the socket. Stopping execution"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error:
        print(SCKT_ERROR)
        sys.exit()


    host = '127.0.0.1'

    port = 8080

    s.bind((host, port))

    s.listen(5)

    print(SV_START)

    print(SV_WAITING)


    while True:
        c,addr = s.accept()
        th = threading.Thread(target=newClient, args=(c,addr))
        th.start()
    c.close()
