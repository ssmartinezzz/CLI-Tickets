import getopt
import socket
import threading
import sys
import signal
from json import JSONDecodeError

import messages
import server_functions
"""
Server main execution file. It could be executed specifying the port number with option -p, Otherwise it would try
establishing connection on 8080 port.
"""
def new_client(clientsocket, address, lock):
    """
    Function that is executed by every single Thread launched from the Server,
    here server's threads try to decode the destination of operation sent by clients
    for doing tasks with tickets from the Database.
    Depending on the destination, threads can call functions for Editing,Inserting, Modifying and Exporting Tickets.
    @param clientsocket: Socket used for establishing connection with Clients
    @param address: Address of a client (Ip,port)
    @param lock: threading.Lock() used for mutex.
    """
    print(messages.SV_THREAD, threading.get_ident())

    print(messages.SV_CONNECTION, address)

    ip, host = clientsocket.getpeername()

    while True:

        try:
            client_opt = clientsocket.recv(1024)

            if client_opt.decode() == 'INSERT':

                server_functions.server_insertion(clientsocket, lock, ip, client_opt)

            elif client_opt.decode() == 'LIST':

                server_functions.server_list(clientsocket, ip, client_opt)

            elif client_opt.decode() == 'EDIT':

                server_functions.server_editTicket(clientsocket, ip, client_opt)

            elif client_opt.decode() == 'EXPORT':

                server_functions.server_exportTicket(clientsocket, ip, client_opt)

            elif client_opt.decode() == 'CLEAR':

                server_functions.server_clear(ip, client_opt)

            elif client_opt.decode() == 'EXIT':

                break

        except JSONDecodeError:

            print(messages.ERR_MSG_COULDNT, ip)

            break

    print(messages.SCK_CLOSED,addr)

    clientsocket.close()

"""def sendMessageAsyn(s, f):
    for sock, addr in socket_list:
        msg = messages.TCKT_CREATED + " \r\n"
        sock.send(msg.encode())
        """

if __name__ == "__main__":

    "Default port instance, could be given by terminal anyway"
    port = 8080

    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')

    for (op, ar) in opt:

        if op == '-p':

            port = int(ar)

    socket_list = []

    "signal.signal(signal.SIGUSR1, sendMessageAsyn)"

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = '0.0.0.0'

        s.bind((host, port))

        s.listen(5)

    except socket.error or PermissionError:

        print(messages.SCKT_ERROR)

        sys.exit()

    print(messages.SCKT_CREATED)

    print(messages.SV_START)

    print(messages.SV_WAITING)

    lock = threading.Lock()

    while True:

        threads_list = list()

        try:

            c, addr = s.accept()

            client_data = c, addr

            socket_list.append(client_data)

            th = threading.Thread(target=new_client, args=(c, addr, lock,))

            threads_list.append(th)

            th.start()

            for thread in threads_list:

                thread.join(0.5)

        except KeyboardInterrupt or EOFError:

            if KeyboardInterrupt:

                print("\n", messages.KYBRD_INTERRUPT)

            elif EOFError:

                print("\n", messages.EOFE)

            sys.exit()











