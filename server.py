import getopt
import socket
import threading
import sys
from json import JSONDecodeError
import messages
import server_functions
"""
Server main execution file. It could be executed specifying the port number with option -p, Otherwise it would try
establishing connection on 8080 port.
"""
def new_client(clientsocket, lock, sem):
    """
    Function that is executed by every single Thread launched from the Server,
    here server's threads try to decode the destination of operation sent by clients
    for doing tasks with tickets from the Database.
    Depending on the destination, threads can call functions for Editing,Inserting, Modifying and Exporting Tickets.
    @param clientsocket: Socket used for establishing connection with Clients
    @param lock: threading.Lock() used for mutex.
    @param sem: threading.Semaphore() used for blocking while editing a Ticket.
    """
    print(messages.SV_THREAD, threading.get_ident())

    ip, host = clientsocket.getpeername()

    print(messages.SV_CONNECTION, ip, host)

    while True:

        try:
            client_opt = clientsocket.recv(1024)

            if client_opt.decode() == 'INSERT':

                server_functions.server_insertion(clientsocket, lock, ip, client_opt)

            elif client_opt.decode() == 'LIST':

                server_functions.server_list(clientsocket, ip, client_opt)

            elif client_opt.decode() == 'EDIT':

                server_functions.server_edit_ticket(clientsocket, ip, client_opt , sem)

            elif client_opt.decode() == 'EXPORT':

                server_functions.server_export_ticket(clientsocket, ip, client_opt)

            elif client_opt.decode() == 'CLEAR':

                server_functions.server_clear(ip, client_opt)

            elif client_opt.decode() == 'EXIT':

                break

            elif not client_opt:

                break

        except JSONDecodeError:

            print(messages.ERR_MSG_COULDNT, ip)

            break

    print(messages.SCK_CLOSED, ip, host)

    clientsocket.close()

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

    lock = threading.Lock() #Recursos compartidos.

    sem = threading.Semaphore()

    while True:

        threads_list = list()

        try:

            c, addr = s.accept()

            client_data = c, addr

            socket_list.append(client_data)

            th = threading.Thread(target=new_client, args=(c, lock, sem,))

            threads_list.append(th)
            "Deamon set"
            th.daemon = True

            th.start()

            for thread in threads_list:

                thread.join(0.5)

        except KeyboardInterrupt:

            print("\n", messages.KYBRD_INTERRUPT)

            sys.exit()

        except EOFError:

            print("\n", messages.EOFE)

            sys.exit()












