import threading

from dbFunctions import *
from filter import *
import signal
from utils import  *

def main_execution(clientsocket,address,lock):

    print(messages.SV_THREAD,threading.get_ident())

    print(messages.SV_CONNECTION, address)

    ip, host = clientsocket.getpeername()

    while True:

        client_opt = clientsocket.recv(1024)

        if client_opt.decode() == 'INSERT':

            clientsocket.send(messages.OPT_ADD_TICK.encode())

            ticketrecv = clientsocket.recv(1024)

            decoded_t = recvJson(ticketrecv.decode())

            addTicket(decoded_t, lock)

            clientsocket.send(messages.TCKT_CREATED.encode())

            generateHistory(ip, client_opt.decode())

            os.kill(os.getpid(), signal.SIGUSR1)

        elif client_opt.decode() == 'LIST':

            clientsocket.send(messages.OPT_LIST_TICK.encode())

            client_filters = clientsocket.recv(1024)

            data_ticket = clientsocket.recv(1024)

            client_filters = client_filters.decode()

            try:
                filters_decoded = json.loads(client_filters)

                data_ticket = recvJson(data_ticket.decode())

                result = filterAction(filters_decoded, data_ticket)

                result = str(result)

                clientsocket.send(result.encode())

                print(messages.TCKTS_LISTED, ip)

            except:

                pass

            generateHistory(ip, client_opt.decode())

        elif client_opt.decode() == 'EDIT':

            clientsocket.send(messages.OPT_EDIT_TICK.encode())

            recievingId = clientsocket.recv(1024)

            recievingId = int(recievingId.decode())

            clientsocket.send(messages.SV_RECV_ID.encode("utf-8"))

            modifiers = clientsocket.recv(1024)

            data_ticket = clientsocket.recv(1024)

            ticketexists = existsTicket(id)

            if ticketexists:

                modifiers = modifiers.decode()

                modifiers_decoded = json.loads(modifiers)

                data_ticket = recvJson(data_ticket.decode())

                params_applied = editionFiltred(recievingId, modifiers_decoded, data_ticket)

                editTicket(recievingId, params_applied)

                edited_ticket = getTicketbyId(recievingId)

                clientsocket.send(dumpTicket(edited_ticket).encode())

                print(messages.TCKT_EDITED, ip)


            else:

                clientsocket.send(messages.ERR_MSG_NOAVAILABLE.encode())

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

            generateHistory(ip, client_opt.decode())

        elif client_opt.decode() == 'EXIT':

            print(messages.SCK_CLOSED, ip)

            break

        if not client_opt:
            break