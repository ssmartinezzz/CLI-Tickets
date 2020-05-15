import socket
import threading
import sys
import messages






def newClient(clientsocket,address):
    print(messages.SV_THREAD)

    print(messages.SV_CONNECTION,address)

    while True:

        clientOpt = clientsocket.recv(1024)

        if (clientOpt.decode() == 'INSERT'):

        if (clientOpt.decode() == 'EXIT'):
            

if __name__ == "__main__":

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error:
        print(messages.SCKT_ERROR)
        sys.exit()
    print(messages.SCKT_CREATED)

    host = '127.0.0.1'

    port = 8080

    s.bind((host, port))

    s.listen(5)

    print(messages.SV_START)

    print(messages.SV_WAITING)


    while True:
        c,addr = s.accept()
        th = threading.Thread(target=newClient, args=(c,addr))
        th.start()
    c.close()
