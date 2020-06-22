import socket
import sys

import getopt

import cliController
from utils import *

import client_functions

if __name__ == "__main__":

    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')

    for (op, ar) in opt:

        if op == '-a':

            host = str(ar)

        elif op == '-p':

            port = int(ar)

    try:

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((host, port))

        print(messages.SCKT_CREATED)

    except socket.error or ConnectionRefusedError:

        print(messages.SCKT_ERROR)

        sys.exit()


    while True:

        try:

            destination = cliController.mainClientCLI()

            if destination == "INSERT":
                try:

                    client_functions.client_ticketInsertion(client, destination)

                except IndexError:

                    print(messages.ERR_MSG_INPUT)

                    break

            elif destination == "LIST":

                client_functions.client_ticketList(client, destination)

            elif destination == "EDIT":

                client_functions.client_ticketEdition(client, destination)

            elif destination == "EXPORT":

                client_functions.client_ticketExport(client, destination)

            elif destination == "CLEAR":

                client_functions.client_clearTerminal(client, destination)

            elif destination == "EXIT":

                client_functions.client_exit(client, destination)

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

        except KeyboardInterrupt or EOFError or BrokenPipeError:

            if KeyboardInterrupt:

                print("\n", messages.KYBRD_INTERRUPT)

            elif EOFError:

                print("\n", messages.EOFE)

            elif BrokenPipeError:
                print("\n",messages.ERR_MSG_BP)

            sys.exit()

    print(messages.OPT_EXIT)

    client.close()





