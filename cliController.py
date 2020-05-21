import getopt

import messages
from parserUtilities import *
from utils import formatDate, checkStatus
from dbFunctions import *


def mainClientCLI():
    print(messages.CLIENT_MENU)

    choosedOption = input("Option ")
    parsedOption = parse_args(choosedOption)

    (option, arg) = getopt.getopt(parsedOption[0:], 'i l e x o', ["insert", "list", "edit", "export", "exit"])

    destination = ('EXIT')
    for op, value in option:

        if op in ('--insert', '-i') and value == '':

            destination = ('INSERT')
        elif op in ('--list', '-l') and value == '':

            destination = ('LIST')
        elif op in ('--edit', '-e') and value == '':

            destination =('EDIT')

        elif op in ('--export', '-x') and value == '':

            destination = ('EXPORT')

        elif op in ('--exit','-o')and value =='':
            destination = ('EXIT')

    return destination

def clientAddCLI():

    print(messages.OPT_ADD_TICK)

    ticket = []

    chosedOPT = input("command: ")

    parsedOPT = parseSpaces(chosedOPT)

    (option, arg) = getopt.getopt(parsedOPT[0:], 't:a:d:')


    for (op, ar) in option:

        if op == '-t':

            title= str(ar)
            ticket.append(title)

        elif op == '-a':
            author = str(ar)
            ticket.append(author)

        elif op == '-d':

            description =str(ar)

            ticket.append(description)

    return ticket

def clientListCLI():


    print(messages.OPT_LIST_TICK)

    chosedOPT = input("command: ")

    parsedOPT = parseSpaces(chosedOPT)

    (option, arg) = getopt.getopt(parsedOPT[0:], 'a:d:s:')

    tickets = listTicketsbyDateAuthOrStatus()

    filters_applied = []

    ticket = {}

    for (op, ar) in option:

        if op == '-a':

            author= str(ar)

            present_author = "author"

            filters_applied.append(present_author)
            ticket['author'] = author

        elif op == '-d':
            date =ar

            searchDate = formatDate(date)

            present_date = "date"

            filters_applied.append(present_date)
            ticket['date'] = searchDate

        elif op == '-s':

            status =str(ar)

            checkStatus(status)

            present_status = "status"

            filters_applied.append(present_status)

            ticket['status'] = status


    if ("author" in filters_applied):

        tickets = tickets.filter( Ticket.author == ticket['author'])

    elif("date"in filters_applied):

       tickets = tickets.filter(Ticket.date == ticket['date'])

    elif("status" in filters_applied):

        tickets = tickets.filter(Ticket.status == ticket['status'])

    result = session.execute(tickets)


    return result.fetchall()

def cliientEditCLI():

    print(messages.OPT_EDIT_TICK)

    chosedOPT = input("command: ")

    parsedOPT = parseSpaces(chosedOPT)

    (option, arg) = getopt.getopt(parsedOPT[0:], 'i:t:d:s:')

    ticket = []
    for (op, ar) in option:
        if op == '-i':

            id = int(ar)


            ticket.append(id)

        elif op == '-t':
            title = ar

            ticket.append(title)

        elif op == '-s':

            status = str(ar)

            checkStatus(status)

            ticket.append(status)
        elif op == '-d':

            description = str(ar)

            ticket.append(description)


    return ticket








