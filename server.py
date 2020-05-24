import multiprocessing
import socket
import threading
import sys
import messages
from utils import  *
from dbFunctions import *
from filter import *
import csv


def newClient(clientsocket, address):

    print(messages.SV_THREAD)

    print(messages.SV_CONNECTION, address)

    ip, host = clientsocket.getpeername()

    lock = threading.Lock()



    while True:
        client_opt = clientsocket.recv(1024)
        if (client_opt.decode() == 'INSERT'):

            ticketrecv = clientsocket.recv(1024)

            decodedT = recvJson(ticketrecv.decode())

            addTicket(decodedT,lock)

            clientsocket.send(messages.TCKT_CREATED.encode())

            generateHistory(ip, client_opt.decode())



        elif (client_opt.decode() == 'LIST'):

            client_filters  = clientsocket.recv(1024)

            data_ticket = clientsocket.recv(1024)

            client_filters = client_filters.decode()

            try:
                filters_decoded = json.loads(client_filters)

                data_ticket = recvJson(data_ticket.decode())

                result = filterAction(filters_decoded, data_ticket)

                result = str(result)

                clientsocket.send(result.encode())

                print(messages.TCKTS_LISTED,ip)

            except:

                pass

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

        elif(client_opt.decode() == 'EXPORT'):

            client_filters = clientsocket.recv(1024)

            data_ticket = clientsocket.recv(1024)

            client_filters = client_filters.decode()

            paralell_p = multiprocessing.Process(target=exportTicket,args=(clientsocket,data_ticket,client_filters,))

            paralell_p.start()

            generateHistory(ip, client_opt.decode())

        elif(client_opt.decode() == 'EXIT'):
            print(messages.SCK_CLOSED, ip)
            break
            
        if not client_opt:
            break


    clientsocket.close()


def exportTicket(socket,dataticket,clientfilters):

    print(messages.SV_PROCESS)

    try:

        tickets = filterExport(clientfilters,dataticket)

        fd = open("tickets.csv", "w", newline="")
        header = ['id', 'title', 'author', 'date', 'description', 'status']
        fd.write(header)
        for row in tickets:
            fd.write(row)

        fd.close()



    except:

        pass




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




