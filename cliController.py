import getopt

import messages
from parserUtilities import parse_args
from utils import formatDate, checkStatus


def mainClientCLI():
    print(messages.CLIENT_MENU)

    choosedOption = input("Option ")
    parsedOption = parse_args(choosedOption)

    (option, arg) = getopt.getopt(parsedOption[0:], 'ilexo', ["insert", "list", "edit", "export", "exit"])

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

    parsedOPT = parse_args(chosedOPT)

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

    parsedOPT = parse_args(chosedOPT)

    (option, arg) = getopt.getopt(parsedOPT[0:], 'a:d:s:')

    ticket =[]
    for (op, ar) in option:

        if op == '-a':

            author= str(ar)

            ticket.append(author)

        elif op == '-d':
            date = ar

            searchDate = formatDate(date)

            ticket.append(searchDate)

        elif op == '-s':

            status =str(ar)

            checkStatus(status)

            ticket.append(status)

    return ticket





