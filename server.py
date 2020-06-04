
import socket
import threading
import sys,os,signal
import time
from multiprocessing import Manager
import messages
from utils import  *
from dbFunctions import *
from filter import *



def newClient(client,current_editing):

    clientsocket, address = client

    print(messages.SV_THREAD)

    print(messages.SV_CONNECTION, address)

    ip, host = clientsocket.getpeername()

    lock = threading.Lock()

    while True:

        client_opt = clientsocket.recv(1024)
        msg = "Done"

        if client_opt.decode() == 'INSERT':

            clientsocket.send(messages.OPT_ADD_TICK.encode())

            ticketrecv = clientsocket.recv(1024)

            decodedT = recvJson(ticketrecv.decode())

            addTicket(decodedT,lock)

            clientsocket.send(messages.TCKT_CREATED.encode())

            generateHistory(ip, client_opt.decode())

            """os.kill(os.getppid(),signal.SIGUSR1)"""

        elif client_opt.decode() == 'LIST':

            clientsocket.send(messages.OPT_LIST_TICK.encode())

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

        elif client_opt.decode() == 'EDIT':

            clientsocket.send(messages.OPT_EDIT_TICK.encode())

            recievingId = clientsocket.recv(1024)

            ticketexists = existsTicket(recievingId)

            if ticketexists:

                time.sleep(3)

                if recievingId not in current_editing:

                    current_editing.append(recievingId)

                    containingTicket = clientsocket.recv(1024)

                    decodedT = recvJson(containingTicket.decode())

                    editTicket(recievingId, decodedT)

                    editedTicket = getTicketbyId(recievingId)

                    clientsocket.send(dumpTicket(editedTicket).encode())

                    print(messages.TCKT_EDITED, ip)



                elif recievingId in current_editing:

                    clientsocket.send(messages.TCKT_CURRENT_EDITING+"\n"+str(recievingId))

            else:

                clientsocket.send(messages.ERR_MSG_NOAVAILABLE.encode())

            current_editing.remove(recievingId)

            generateHistory(ip, client_opt.decode())

        elif client_opt.decode() == 'EXPORT':

            clientsocket.send(messages.OPT_EXPORT_TICK.encode())

            client_filters = clientsocket.recv(1024)

            data_ticket = clientsocket.recv(1024)

            client_filters = client_filters.decode()


            try:
                filters_decoded = json.loads(client_filters)

                data_ticket = recvJson(data_ticket.decode())

                result = filterAction(filters_decoded, data_ticket)

                result = str(result)

                clientsocket.send(result.encode())

                print(messages.NEW_PROCESS, ip)

            except:

                pass

            generateHistory(ip, client_opt.decode())

        elif client_opt.decode() == 'CLEAR':

            generateHistory(ip,client_opt.decode())

        elif client_opt.decode() == 'EXIT':

            print(messages.SCK_CLOSED, ip)

            break
            
        if not client_opt:
            break

    """clientsocket.send(msg.encode("ascii"))"""
    clientsocket.close()

def sendAsyn(s,f):

    for sock,addr in socket_list:

        sock.send(messages.TCKT_BRD_CRATED.encode("ascii"))




if __name__ == "__main__":
    socket_list = []

    signal.signal(signal.SIGUSR1,sendAsyn)
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

    manager = Manager()
    current_editing = manager.list()
    while True:

        client_data = s.accept()

        socket_list.append(client_data)

        th = threading.Thread(target=newClient, args=(client_data,current_editing ))

        th.start()




