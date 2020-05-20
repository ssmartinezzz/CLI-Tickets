import datetime
import messages
import os


def formatDate(date):

    return datetime.datetime.strptime(date, "%d/%m/%Y")



def idValidator(id):

    try:

        int(id)

        return True

    except ValueError:

        return False

def checkStatus(status):

    if ((status == "pending") |(status == "in process") |(status == "solved")):

        pass

    else:

        print(messages.ERR_MSG_STATUS)



def generateHistory(address ,operation):

    log = open('Historial.log', 'a')

    log.write("\n")

    log.write(f"\nThe client:{address} operation: {operation} Date:{datetime.datetime.now()}$")

    log.close()

def clearTerminal():

    os.system('clear')







