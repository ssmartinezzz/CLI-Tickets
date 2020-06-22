import sys

import cliController
import multiprocessing
import messages
from jsonService import *
import time

from utils import *


def exportTickets(socket,filtersapplied,ticketData):

    socket.send(filtersapplied.encode())

    socket.send(ticketData.encode())

    ticket_search = socket.recv(1024)

    ticket_search = ticket_search.decode()

    list_tickets = eval(ticket_search)

    generateCSV(list_tickets)

    print(messages.CLIENT_EXPORT_SUCCESS)

def client_ticketInsertion(client,destination):
    clearTerminal()

    client.send(destination.encode())

    print(client.recv(1024).decode())

    cliTick = cliController.clientAddCLI()

    ticket = {'title': cliTick[0], 'author': cliTick[1], 'description': cliTick[2]}

    client.send(sendJson(ticket).encode())

    print(client.recv(1024).decode())

def client_ticketList(client, destination):

    client.send(destination.encode())

    clearTerminal()

    print(client.recv(1024).decode())

    filtersapplied, ticketData = cliController.clientListCLI()

    filtersapplied = sendJson(filtersapplied)

    ticketData = sendJson(ticketData)

    client.send(filtersapplied.encode())

    client.send(ticketData.encode())

    ticket_search = client.recv(1024)

    ticket_search = ticket_search.decode()

    list_tickets = eval(ticket_search)

    printableTicket(list_tickets)

def client_ticketEdition(client,destination):

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

    client.send(destination.encode())

    clearTerminal()

    print(client.recv(1024).decode())

    filtersapplied, ticketData = cliController.clientListCLI()

    filtersapplied = sendJson(filtersapplied)

    ticketData = sendJson(ticketData)

    paralell_p = multiprocessing.Process(target=exportTickets, args=(client, filtersapplied, ticketData,))

    paralell_p.start()

    time.sleep(2)

    paralell_p.join()

def client_clearTerminal(client, destination):

    clearTerminal()

    client.send(destination.encode())

def client_exit(client, destination):
    clearTerminal()

    client.send(destination.encode())



