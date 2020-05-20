import socket
import sys
from dbFunctions import *
import getopt
import messages
from jsonService import *
from utils import *
import cliController


if __name__ == "__main__":

    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

    for (op, ar) in opt:

        if op == '-a':

            host = str(ar)

        elif op == '-p':

            port = int(ar)

    try:

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error:

        print(messages.SCKT_ERROR)

        sys.exit()

    print(messages.SCKT_CREATED)

    client.connect((host, port))

    while True:

        destination = cliController.mainClientCLI()

        if destination == ("INSERT"):
            clearTerminal()

            client.send(destination.encode())

            cliTick = cliController.clientAddCLI()

            ticket = {'title': cliTick[0], 'author': cliTick[1], 'description': cliTick[2]}

            client.send(sendJson(ticket).encode())

            print(client.recv(1024).decode())



        elif destination == ("LIST"):

            clearTerminal()

            client.send(destination.encode())

            ticketSearch = cliController.clientListCLI()

            filter = {'author': ticketSearch[0], 'date': convertDateJson(ticketSearch[1]), 'status': ticketSearch[2]}

            client.send(sendJson(filter).encode())

            searchResult = client.recv(2048)

            print(recvJson(searchResult.decode()))


        elif destination == ("EDIT"):

            clearTerminal()

            client.send(destination.encode())

            ticketToedit = cliController.cliientEditCLI()

            if (idValidator(ticketToedit[0]) == True):

                ticketexists = existsTicket(ticketToedit[0])

                if (ticketexists):

                    client.send(str(ticketToedit[0]).encode())

                    edit = {'title': ticketToedit[1], 'status': ticketToedit[2], 'description': ticketToedit[3]}

                    client.send(sendJson(edit).encode())

                    editedTicket = client.recv(1024)

                    print(recvJson(editedTicket.decode()))

                else:

                    print(messages.ERR_MSG_NOAVAILABLE)



            else:
                print(messages.ERR_MSG_INPUT)


        elif destination == ("EXIT"):
            clearTerminal()
            client.send(destination.encode())
            break

        else:
            print(messages.OPT_WRONG)

    print(messages.OPT_EXIT)

    client.close()



