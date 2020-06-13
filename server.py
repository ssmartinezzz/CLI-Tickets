import getopt
import socket
import threading
import sys
import signal
import messages
import server_functions


def newClient(clientsocket, address, lock):

    server_functions.main_execution(clientsocket,address,lock)
    print(messages.SCK_CLOSED,addr)

    clientsocket.close()

def sendMessageAsyn(s, f):
    for sock, addr in socket_list:
        msg = messages.TCKT_CREATED + " \r\n"
        """sock.send(msg.encode())"""

if __name__ == "__main__":

    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')

    for (op, ar) in opt:

        if op == '-p':

            port = int(ar)

    socket_list = []
    signal.signal(signal.SIGUSR1, sendMessageAsyn)

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error:
        print(messages.SCKT_ERROR)
        sys.exit()
    print(messages.SCKT_CREATED)

    host = '0.0.0.0'



    s.bind((host, port))

    s.listen(5)

    print(messages.SV_START)

    print(messages.SV_WAITING)

    lock = threading.Lock()

    while True:
        c, addr = s.accept()

        client_data = c,addr

        socket_list.append(client_data)

        th = threading.Thread(target=newClient, args=(c, addr,lock,))

        th.start()




