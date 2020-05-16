import socket
import sys
import os
import getopt
import messages
from jsonService import *
from utils import *

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
        print(messages.CLIENT_MENU)

        chosenOption = input('Option: ').upper()

        client.send(chosenOption.encode())

        if (chosenOption == 'INSERT'):

            print(messages.OPT_ADD_TICK, messages.ADD_TITLE)

            tTitle = input()

            print(messages.ADD_AUTHOR)

            tAuth = input()

            print(messages.ADD_DESCRIPTION)

            tDescr = input()

            ticket = {'title':tTitle,'author':tAuth,'description':tDescr}

            sendJson(client,ticket)



        elif (chosenOption == 'LIST'):

            print(messages.OPT_LIST_TICK,messages.ADD_AUTHOR)

            searchAuth = input()

            print(messages.SRCH_DATE)

            searchDate = input()

            searchDate = formatDate(searchDate)

            print(messages.SRCH_STATUS)

            searchStatus = input()

            filter = {'author':searchAuth,'date':convertDateJson(searchDate),'status':searchStatus}

            sendJson(client,filter)

            searchResult = client.recv(1024)

            print(searchResult.decode())

        elif (chosenOption == 'EDIT'):

            print(messages.OPT_EDIT_TICK)

        elif (chosenOption == 'FILTER'):

            print(messages.OPT_FILTER_TICK)

        elif (chosenOption == 'EXIT'):

            print(messages.OPT_EXIT)

            break

        else:
            print(messages.OPT_WRONG)

    client.close()
