import socket
import threading
import sys
import messages
from dbFunctions import *


def newClient(clientsocket, address):
    print(messages.SV_THREAD)

    print(messages.SV_CONNECTION, address)

    lock = threading.Lock()

    client_opt = clientsocket.recv(1024)

    if (client_opt.decode() == 'INSERT'):
        addTicket(clientsocket, lock)

    elif (client_opt.decode() == 'LIST'):
        ticketSearch = listTicketsbyDateAuthOrStatus(clientsocket)

        clientsocket.send(sendTicketsToJson(ticketSearch).encode())

    elif (client_opt.decode() == 'EDIT'):

        ticketexists = existsTicket(clientsocket.recv(1024))
        if (ticketexists):

            ticketFound = getTicketbyId(ticketexists)

            clientsocket.send(messages.TCKT_FOUND.encode() + dumpTicket(ticketFound).encode())

        else:

            clientsocket.send(messages.ERR_MSG_NOAVAILABLE.encode())
















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
        c, addr = s.accept()

        th = threading.Thread(target=newClient, args=(c, addr))

        th.start()

        th.join()

        c.close()
