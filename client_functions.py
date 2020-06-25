import sys
import cliController
import multiprocessing
import messages
from jsonService import *
import time
from utils import *

def exportTickets(socket, filtersapplied, ticketData):
    """
    function executed in a paralell process with @client_ticketExport
    that search Tickets depending on the filters applied and then export
    them to a csv compressed file (gz)
    @param socket: (Socket object where the connection between Server - Client is established
    and can send or receive data through it)
    @param filtersapplied: (list of filters inserted in the command line
    by the client. Any - author - description - date)
    @param ticketData:(Values that are going to be applied to search using filters)
    """
    socket.send(filtersapplied.encode())

    socket.send(ticketData.encode())

    ticket_search = socket.recv(1024)

    ticket_search = ticket_search.decode()

    list_tickets = eval(ticket_search)

    if list_tickets[0] == messages.ERR_MSG_NOAVAILABLE:

        print(messages.ERR_MSG_NOAVAILABLE)

    else:

        generateCSV(list_tickets)

        print(messages.CLIENT_EXPORT_SUCCESS)

def client_ticketInsertion(client, destination):
    """
    function that allows a client to send the specific values required
    to insert a new Ticket object in the database.
    @param client: (Is the socket connection where the data is sent or recieved)
    @param destination: The main action that is executed, e.g List | Insert | export).
    This value is sent to the Server.
    """
    clearTerminal()

    client.send(destination.encode())

    print(client.recv(1024).decode())

    cliTick = cliController.clientAddCLI()

    ticket = {'title': cliTick[0], 'author': cliTick[1], 'description': cliTick[2]}

    client.send(sendJson(ticket).encode())

    print(client.recv(1024).decode())

def client_ticketList(client, destination):
    """
    function that allows a client to send the
    different values needed to list an existing Ticket
    @param client:(Is the socket connection where the data is sent or recieved)
    @param destination:(The main action that is executed, e.g List | Insert | export)
    """
    client.send(destination.encode())

    clearTerminal()

    print(client.recv(1024).decode())

    filtersapplied, ticketData = cliController.filteredCLI()

    filtersapplied = sendJson(filtersapplied)

    ticketData = sendJson(ticketData)

    client.send(filtersapplied.encode())

    client.send(ticketData.encode())

    ticket_search = client.recv(1024)

    ticket_search = ticket_search.decode()

    list_tickets = eval(ticket_search)

    print(list_tickets)

def client_ticketEdition(client, destination):
    """
    function that enable a client to edit a ticket
    by giving an ID value and the modifications of it.
    This function verifies if the given ID format is correct by using
    @idValidator and it verifies through the server if the correct format
    given id exist on the DB.
    @param client: (Socket Object for communication)
    @param destination: (value of the current action that is being executed)
    """
    clearTerminal()

    client.send(destination.encode())

    print(client.recv(1024).decode())

    modifiers, ticket_toedit = cliController.cliientEditCLI()

    correct_input_id = idValidator(ticket_toedit['id'])

    if correct_input_id:

        id = ticket_toedit['id']

        modifiers = sendJson(modifiers)

        ticket_toedit = sendJson(ticket_toedit)

        client.send(str(id).encode())

        if client.recv(1024).decode("utf-8") == "EXISTS":

            client.send(modifiers.encode())

            client.send(ticket_toedit.encode())

            editedTicket = client.recv(1024)

            print(recvJson(editedTicket.decode()))

        else:
            print(messages.ERR_MSG_NOAVAILABLE)
    else:
        sys.exit()

def client_ticketExport(client, destination):
    """
    Main function used for ticket exportation. It launches a parallel process
    using multiprocessing.Process().The parallel process recieves tickets and put them in a compressed CSV file
    @param client: (Socket object for connections and communications)
    @param destination: (Value of the specific task that is being executed)
    """
    client.send(destination.encode())

    clearTerminal()

    print(client.recv(1024).decode())

    filtersapplied, ticketData = cliController.filteredCLI()

    filtersapplied = sendJson(filtersapplied)

    ticketData = sendJson(ticketData)

    paralell_p = multiprocessing.Process(target=exportTickets, args=(client, filtersapplied, ticketData,))

    paralell_p.start()

    time.sleep(2)

    paralell_p.join()

def client_clearTerminal(client, destination):
    """
    function that clears clients's terminals.
    @param client: (Socket object for communication)
    @param destination: (Value of the current action that is sent to the server through the socket object)
    """
    clearTerminal()

    client.send(destination.encode())

def client_exit(client, destination):
    """
    function that disconnects the client from the server.
    After sending the destination value, the connection will be closed.
    @param client: (Socket object)
    @param destination: (Value of the operation executed, is sent to the server through the socket object)

    """
    clearTerminal()

    client.send(destination.encode())



