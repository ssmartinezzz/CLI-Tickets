import datetime
import messages
import os
import csv
import gzip
"""
This file has different utilities that are implemented in other functions 
"""

def date_format(date):
    """
    This function convert a instance of datetime.datetime into a string
    @param date:  instance of datetime.datetime
    @return: string containing a date with dd/mm/yyyy format

    """
    return str(datetime.datetime.strptime(date, "%d/%m/%Y"))

def id_validator(id):
    """
    This function verifies if a given ID is an int type.
    @param id: input id which is going to be checked
    @return: returns a boolean depending on the result.
    """
    try:

        int(id)

        return True

    except ValueError:
        print(messages.ERR_MSG_INPUT)
        return False

def check_status(status):
    """
    This function checks if a given status matches with the acceptable
    ones, otherwise it would raise a ValueError
    @param status: status value of Ticket object
    """

    valid_status = ["pending",
                    "in process",
                    "solved"]

    if status in valid_status:
        pass

    else:
        raise ValueError

def generate_csv(tickets):
    """
    This function puts a list of Tickets Objects into a CSV file
    an compress it in a resulting gz file.
    @param tickets: list of tickets filtered
    """
    with gzip.open("tickets.csv.gz", "wt", newline="") as file:
        writer = csv.writer(file)
        titles = ["Id", "Title", "Author", "Date", "Description", "Status"]
        writer.writerow(titles)
        for ticket in tickets:
            writer.writerow((ticket['id'],
                             ticket['title'],
                             ticket['author'],
                             ticket['date'],
                             ticket['description'],
                             ticket['status'],
                             ))


def generate_history(address, operation):
    """
    This function generates a .log file as a history where
    clients adresses and operations are shown with the exact time
    that the server did that operation
    @param address: ip address of a client.
    @param operation: operation done by the client.
    """
    log = open('Historial.log', 'a')

    log.write("\n")

    log.write(f"\nThe client:{address} operation: {operation} Date:{datetime.datetime.now()}$")

    log.close()

def printableTicket(d):
   for key in d:
       print("==============================","\n\n","#Ticket Id:",key['id'],"\n",

       "Title:",key['title'],"\n",

       "Author:",key['author'],"\n",

       "Date:",key['date'],"\n",

       "Description:",key['description'],"\n",

       "Status:",key['status'],"\n\n")


def clear_terminal():
    """
    Function that clears a terminal screen.
    """
    os.system('clear')







