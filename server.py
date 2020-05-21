import socket
import threading
import sys
import messages
from utils import  *
from dbFunctions import *


def newClient(clientsocket, address):

    print(messages.SV_THREAD)

    print(messages.SV_CONNECTION, address)
    ip, host = clientsocket.getpeername()
    lock = threading.Lock()
    page = 1
    pageSize = 6

    client_opt = clientsocket.recv(1024)

    while True:

        if (client_opt.decode() == 'INSERT'):

            ticketrecv = clientsocket.recv(1024)

            decodedT = recvJson(ticketrecv.decode())

            addTicket(decodedT,lock)

            clientsocket.send(messages.TCKT_CREATED.encode())

            generateHistory(ip, client_opt.decode())


        elif (client_opt.decode() == 'LIST'):

            generateHistory(ip, client_opt.decode())

        elif (client_opt.decode() == 'EDIT'):

            generateHistory(ip, client_opt.decode())

            recievingId = clientsocket.recv(1024)

            ticketexists = existsTicket(recievingId)

            if (ticketexists):

                containingTicket = clientsocket.recv(1024)

                decodedT = recvJson(containingTicket.decode())

                editTicket(recievingId, decodedT , lock)

                editedTicket = getTicketbyId(recievingId)

                clientsocket.send(dumpTicket(editedTicket).encode())

            else:

                clientsocket.send(messages.ERR_MSG_NOAVAILABLE.encode())
        elif(client_opt.decode() == 'EXIT'):

            break


    clientsocket.close()

    print(messages.SCK_CLOSED,ip)






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




