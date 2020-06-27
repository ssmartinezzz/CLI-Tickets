import socket
import sys

import getopt

import cliController
from utils import *

import client_functions

if __name__ == "__main__":
    """
    main client function that tries to connect to the server by using a socket.
    
    For creating the client socket, is required to specify two arguments when client.py is executed
    
    @var a: It's the server ip address.
    
    @var p: It's the server port number where the connection is going to be attended
    
    step1: After a correct creation of the socket, the client will recieve the different options available for operating.

    step2: When an operation is completed,the main options will be shown again. {Insert,List,Edit,Export,Clear,exit}
    
    """

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

        except KeyboardInterrupt:

            print("\n", messages.KYBRD_INTERRUPT)

            sys.exit()

        except EOFError:

            print("\n", messages.EOFE)

            sys.exit()

        except BrokenPipeError:

            print("\n", messages.ERR_MSG_BP)

            sys.exit()

    print(messages.OPT_EXIT)

    client.close()





