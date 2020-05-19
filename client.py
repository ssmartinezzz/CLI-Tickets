import socket
import sys
import os
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

    destination = cliController.mainClientCLI()

    if destination == ("INSERT"):

        client.send(destination.encode())

        cliTick = cliController.clientAddCLI()

        ticket = {'title': cliTick[0], 'author': cliTick[1], 'description': cliTick[2]}

        sendJson(client, ticket)



    elif destination == ("LIST"):

        client.send(destination.encode())

        ticketSearch = cliController.clientListCLI()

        filter = {'author': ticketSearch[0], 'date': convertDateJson(ticketSearch[1]), 'status': ticketSearch[2]}

        sendJson(client, filter)

        searchResult = client.recv(1024)

        print(searchResult.decode())

    elif destination == ("EDIT"):

        client.send(destination.encode())

        print(messages.OPT_EDIT_TICK)

        ticketId = input()

        if (idValidator(ticketId) == True):

            client.send(ticketId.encode())

            print(client.recv(1024).decode())

        else:
            print(messages.ERR_MSG_INPUT)


    elif destination ==("EXIT"):

        print(messages.OPT_EXIT)

    else:
         print(messages.OPT_WRONG)

    client.close()
