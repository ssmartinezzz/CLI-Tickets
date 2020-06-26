import sys
import threading
from json import JSONDecodeError

from dbFunctions import *
from filter import *
import signal
from utils import  *

def server_insertion(clientsocket, lock, ip, client_opt):
    """
    Function that is executed in the Server when clients want to insert a new Ticket
    Actually, this function is in charge of receiving data of Tickets through
    the socket, then loads into Json that decoded data.

    After that sequence, this function calls the DB function add_ticket() passing all data received
    for adding Tickets to the db using mutex, and finally, adds to the history the client's ip address +
    the name of the operation done.
    @param clientsocket: Socket Object where the connection is established.
    @param lock: threading.Lock() instance implemented for mutex
    @param ip: IP address of a client, used for History
    @param client_opt: Destination, main option chosen by client for History
    """
    clientsocket.send(messages.OPT_ADD_TICK.encode())

    ticketrecv = clientsocket.recv(1024)

    decoded_t = recv_json(ticketrecv.decode())

    add_ticket(decoded_t, lock)

    clientsocket.send(messages.TCKT_CREATED.encode())

    generate_history(ip, client_opt.decode())

    "os.kill(os.getpid(), signal.SIGUSR1)"

def server_list(clientsocket, ip, client_opt):
    """
    Function that is called by server's threads to list Tickets.

    It gets the 'modifiers' and 'values' of the filters that clients want to apply.
    Then, it loads into JSON that decoded data, and calls function named filter_action() by passing
    that data and gets a list of filtered tickets.

    It sends a filtered list of Tickets through a socket depending on
    what commands a client inserted.

    Finally, it adds to the History the IP address of the client and the name of the operation he did.
    @param clientsocket: Socket Object where server's threads get and send data.
    @param ip: IP address of a client.
    @param client_opt: Option chosen by a client.
    """
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

def server_edit_ticket(clientsocket, ip, client_opt):
    """
    Function that allows the server's thread to edit a ticket given its ID.

    First, it gets an ID and verifies if it exists on the Database using a function called
    exists_ticket which returns a boolean. If that result is True the editing task will continue, otherwise
    it will send an error message through the socket.

    If exists_ticket returns True, the socket object used in this function will wait to get
    params applied and values needed to edit the ticket with the given ID. After getting
    that values it will call edit_ticket function and edit that ticket.

    Finally, when edition is over, the socket will send the resulting ticket to the client and
    will write on the history client's IP address and the operation chosen.
    @param clientsocket: Socket Object where the data is got and sent
    @param ip: Ip address of a client
    @param client_opt: Option chosen by client.
    """
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

def server_export_ticket(clientsocket, ip, client_opt):
    """
    Function that receives filters from the client for
    returning through the socket a filtered list of tickets.
    It will get those filters and then call filter_action() by passing them.

    filter_action will return a List containing all filtered tickets which is going to be sent through the socket.

    Finally, generate_history() is going to be executed where client's ip and operation are added to the log file.

    @param clientsocket: Socket Object where data is got and received.
    @param ip: IP address of a client
    @param client_opt: Option chosen by a client.
    """
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

def server_clear(ip, client_opt):
    """
    Function that inserts the client's ip address and "CLEAR" option to the History

    @param ip: client's ip address
    @param client_opt: Option chosen by the client. In this case is always "CLEAR"
    """
    print(messages.CLIENT_CLEARED, ip)

    generate_history(ip, client_opt.decode())
