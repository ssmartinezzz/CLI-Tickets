import cliController
import multiprocessing
import messages
from jsonService import *
import time
from dbFunctions import *
from utils import *


def exportTickets(socket,filtersapplied,ticketData):

    socket.send(filtersapplied.encode())

    socket.send(ticketData.encode())

    ticket_search = socket.recv(1024)

    ticket_search = ticket_search.decode()

    list_tickets = eval(ticket_search)

    generateCSV(list_tickets)

    print(messages.CLIENT_EXPORT_SUCCESS)

def main_execution(client):
    while True:

        destination = cliController.mainClientCLI()

        if destination == "INSERT":

            clearTerminal()

            client.send(destination.encode())

            print(client.recv(1024).decode())

            cliTick = cliController.clientAddCLI()

            ticket = {'title': cliTick[0], 'author': cliTick[1], 'description': cliTick[2]}

            client.send(sendJson(ticket).encode())

            print(client.recv(1024).decode())

        elif destination == "LIST":

            client.send(destination.encode())

            clearTerminal()

            print(client.recv(1024).decode())

            filtersapplied,ticketData = cliController.clientListCLI()

            filtersapplied = sendJson(filtersapplied)

            ticketData = sendJson(ticketData)

            client.send(filtersapplied.encode())

            client.send(ticketData.encode())

            ticket_search = client.recv(1024)

            ticket_search = ticket_search.decode()

            list_tickets = eval(ticket_search)

            printableTicket(list_tickets)

        elif destination == "EDIT":

            clearTerminal()

            client.send(destination.encode())

            print(client.recv(1024).decode())

            modifiers, ticket_toedit = cliController.cliientEditCLI()

            if idValidator(ticket_toedit['id']):

                ticket_exists = existsTicket(ticket_toedit['id'])

                if ticket_exists:

                    id = ticket_toedit['id']

                    modifiers = sendJson(modifiers)

                    ticket_toedit = sendJson(ticket_toedit)

                    client.send(str(id).encode())

                    print(client.recv(1024).decode("utf-8"))

                    client.send(modifiers.encode())

                    client.send(ticket_toedit.encode())

                    editedTicket = client.recv(1024)

                    print(recvJson(editedTicket.decode()))

                else:

                    print(messages.ERR_MSG_NOAVAILABLE)


        elif destination == "EXPORT":

            client.send(destination.encode())

            clearTerminal()

            print(client.recv(1024).decode())

            filtersapplied, ticketData = cliController.clientListCLI()

            filtersapplied = sendJson(filtersapplied)

            ticketData = sendJson(ticketData)

            paralell_p = multiprocessing.Process(target=exportTickets, args=(client,filtersapplied,ticketData,))

            paralell_p.start()

            time.sleep(2)

            paralell_p.join()

        elif destination == "CLEAR":

            clearTerminal()

            client.send(destination.encode())

        elif destination == "EXIT":

            clearTerminal()

            client.send(destination.encode())

            break
        else:

            print(messages.OPT_WRONG)

    """ client.settimeout(0.5)

           try:

               message = client.recv(1024).decode()
               if not message: break
           except socket.timeout:
               pass
           """

