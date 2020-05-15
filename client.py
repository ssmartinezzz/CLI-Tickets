import socket
import sys
import os
import getopt
import messages



if __name__ == "__main__":

    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

    for (op, ar) in opt:

        if op == '-a':

            a = str(ar)

        elif op == '-p':

            p = int(ar)

    host = a

    port = p

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

            print(messages.OPT_ADD_TICK,messages.ADD_TITLE)

            tTitle = input()

            client.send(tTitle.encode())

            print(messages.ADD_AUTHOR)

            tAuth = input()

            client.send(tAuth.encode())

            print(messages.ADD_DESCRIPTION)

            tDescr = input()

            client.send(tDescr.encode())

        elif (chosenOption == 'LIST'):

            print(messages.OPT_LIST_TICK)

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
