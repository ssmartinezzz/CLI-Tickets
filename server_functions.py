import sys
import threading
from json import JSONDecodeError

from dbFunctions import *
from filter import *
import signal
from utils import  *

def server_insertion(clientsocket, lock,ip,client_opt):

    clientsocket.send(messages.OPT_ADD_TICK.encode())

    ticketrecv = clientsocket.recv(1024)

    decoded_t = recv_json(ticketrecv.decode())

    add_ticket(decoded_t, lock)

    clientsocket.send(messages.TCKT_CREATED.encode())

    generate_history(ip, client_opt.decode())

    os.kill(os.getpid(), signal.SIGUSR1)

def server_list(clientsocket,ip,client_opt):

    clientsocket.send(messages.OPT_LIST_TICK.encode())

    client_filters = clientsocket.recv(1024)

    data_ticket = clientsocket.recv(1024)

    client_filters = client_filters.decode()

    filters_decoded = json.loads(client_filters)

    data_ticket = recv_json(data_ticket.decode())

    result = filter_action(filters_decoded, data_ticket)

    result = str(result)

    clientsocket.send(result.encode())

    print(messages.TCKTS_LISTED, ip)

    generate_history(ip, client_opt.decode())

def server_editTicket(clientsocket,ip,client_opt):

    clientsocket.send(messages.OPT_EDIT_TICK.encode())

    recievingId = clientsocket.recv(1024)

    recievingId = recievingId.decode()

    ticketexists = exists_ticket(recievingId)

    if ticketexists == True:

        msg = "EXISTS"

        clientsocket.send(msg.encode())

        modifiers = clientsocket.recv(1024)

        data_ticket = clientsocket.recv(1024)

        modifiers = modifiers.decode()

        modifiers_decoded = json.loads(modifiers)

        data_ticket = recv_json(data_ticket.decode())

        params_applied = edition_filter(recievingId, modifiers_decoded, data_ticket)

        edit_ticket(recievingId, params_applied)

        edited_ticket = getticketbyid(recievingId)

        clientsocket.send(dumpTicket(edited_ticket).encode())

        print(messages.TCKT_EDITED, ip)

    else:

        clientsocket.send(messages.ERR_MSG_NOAVAILABLE.encode())

    generate_history(ip, client_opt.decode())

def server_exportTicket(clientsocket,ip,client_opt):

    clientsocket.send(messages.OPT_EXPORT_TICK.encode())

    client_filters = clientsocket.recv(1024)

    data_ticket = clientsocket.recv(1024)

    client_filters = client_filters.decode()

    filters_decoded = json.loads(client_filters)

    data_ticket = recv_json(data_ticket.decode())

    result = filter_action(filters_decoded, data_ticket)

    result = str(result)

    clientsocket.send(result.encode())

    print(messages.NEW_PROCESS, ip)

    generate_history(ip, client_opt.decode())

def server_clear(ip,client_opt):

    print(messages.CLIENT_CLEARED, ip)

    generate_history(ip, client_opt.decode())
