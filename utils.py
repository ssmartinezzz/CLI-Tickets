import datetime
import messages
import os


def formatDate(date):

    return str(datetime.datetime.strptime(date, "%d/%m/%Y"))



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

def printableTicket(d):
   for key in d:
       print("Id:",key['id'])

       print("Title:",key['title'])

       print("Author:",key['author'])

       print("Date:",key['date'])

       print("Description:",key['description'])

       print("Status:",key['status'])




def clearTerminal():

    os.system('clear')







