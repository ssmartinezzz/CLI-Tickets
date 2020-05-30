import datetime
import messages
import os
import csv


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

def generateCSV(tickets):
    with open('tickets.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        titles = ["Id", "Title", "Author", "Date", "Description", "Status"]
        writer.writerow(titles)
        for ticket in tickets:
            writer.writerow((ticket['id'],
                             ticket['title'],
                             ticket['author'],
                             ticket['date'],
                             ticket['description'],
                             ticket['status']))
        f_handle.close()


def generateHistory(address ,operation):

    log = open('Historial.log', 'a')

    log.write("\n")

    log.write(f"\nThe client:{address} operation: {operation} Date:{datetime.datetime.now()}$")

    log.close()

def printableTicket(d):
   for key in d:
       print("Id:",key['id'],"\n",

       "Title:",key['title'],"\n",

       "Author:",key['author'],"\n",

       "Date:",key['date'],"\n",

       "Description:",key['description'],"\n",

       "Status:",key['status'],"\n",
             "-------------------------------------")


def clearTerminal():

    os.system('clear')







