import socket
import sys

import getopt

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

    client_functions.main_execution(client,)

    print(messages.OPT_EXIT)

    client.close()





