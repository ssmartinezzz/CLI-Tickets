import getopt
import time
import messages
from parserUtilities import *
from utils import formatDate, checkStatus



def mainClientCLI():
    print(messages.CLIENT_MENU)

    choosedOption = input("Option ")

    parsedOption = parseSpaces(choosedOption)

    (option, arg) = getopt.getopt(parsedOption[0:], 'i l e x o c', ["insert", "list", "edit", "export", "exit","clear"])

    destination = ('EXIT')

    for op, value in option:

        if op in ('--insert', '-i'):

            destination = ('INSERT')

        elif op in ('--list', '-l'):

            destination = ('LIST')

        elif op in ('--list','-l'):

            destination= ('LIST')

        elif op in ('--edit', '-e'):

            destination =('EDIT')

        elif op in ('--export', '-x'):

            destination = ('EXPORT')

        elif op in ('--exit','-o'):

            destination = ('EXIT')

        elif op in('--clear','-c' ) :

            destination = ('CLEAR')

    return destination

def clientAddCLI():

    ticket = []

    time.sleep(1)

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

    chosed_opt = input("command:")

    parsed_opt = parseSpaces(chosed_opt)

    (option, arg) = getopt.getopt(parsed_opt[0:], 'p:a:d:s:v')

    filters_applied = []

    ticket = {}

    for (op, ar) in option:

        if op == '-p':
            pagination = int(ar)

            present_pagination = "pagination"

            filters_applied.append(present_pagination)

            ticket['pagination'] = pagination

        elif op == '-a':

            author= str(ar)

            present_author = "author"

            filters_applied.append(present_author)

            ticket['author'] = author

        elif op == '-d':

            date = ar

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

        elif op =='-v':
            none_filters = str(ar)

            without_filters ="without"

            filters_applied.append(without_filters)

            ticket['without'] = none_filters

    return filters_applied, ticket

def cliientEditCLI():

    chosedOPT = input("command: ")

    parsedOPT = parseSpaces(chosedOPT)

    (option, arg) = getopt.getopt(parsedOPT[0:], 'i:t:d:s:')

    modifiers = []

    ticket = {}
    for (op, ar) in option:
        if op == '-i':

            id = int(ar)

            present_id = "id"

            modifiers.append(present_id)

            ticket['id'] = id

        elif op == '-t':
            title = ar

            present_title = "title"

            modifiers.append(present_title)

            ticket['title']=title

        elif op == '-s':

            status = str(ar)

            checkStatus(status)

            present_status ="status"

            modifiers.append(present_status)

            ticket['status'] = (status)
        elif op == '-d':

            description = str(ar)

            present_description = "description"

            modifiers.append(present_description)

            ticket['description'] = description

    return modifiers,ticket







