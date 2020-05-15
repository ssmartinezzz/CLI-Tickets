import socket
import sys
import os
import getopt





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
        print('Fallo al crear el socket!')
        sys.exit()

    print('Socket Creado!')


    client.connect((host, port))

    while True:
        print("Send a message to the server!")
        msg = input()
        client.send(msg.encode())
    client.close()
