import getopt
import sys
import time
from parserUtilities import *
from utils import *



def mainClientCLI():
    print(messages.CLIENT_MENU)

    choosedOption = input("Option ")

    parsedOption = parseSpaces(choosedOption)

    try:
        (option, arg) = getopt.getopt(parsedOption[0:], 'i l e x o c',
                                      ["insert", "list", "edit", "export", "exit", "clear"])

    except getopt.GetoptError as err:

        print(str(err))

        sys.exit()



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

    try:

        (option, arg) = getopt.getopt(parsedOPT[0:], 't:a:d:')

    except getopt.GetoptError as err:

        print(str(err))

        sys.exit()



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

    try:

        (option, arg) = getopt.getopt(parsed_opt[0:], 'p:a:d:s:v')

    except getopt.GetoptError as err:

        print(str(err))

        sys.exit()


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

            try:
                searchDate = formatDate(date)

                present_date = "date"

                filters_applied.append(present_date)

                ticket['date'] = searchDate

            except ValueError:

                print(messages.ERR_MSG_DATE)

                sys.exit()

        elif op == '-s':

            status =str(ar)

            try:
                checkStatus(status)

                present_status = "status"

                filters_applied.append(present_status)

                ticket['status'] = status

            except ValueError:

                print(messages.ERR_MSG_STATUS)

                sys.exit()



        elif op =='-v':
            none_filters = str(ar)

            without_filters ="without"

            filters_applied.append(without_filters)

            ticket['without'] = none_filters

    return filters_applied, ticket

def cliientEditCLI():

    chosedOPT = input("command: ")

    parsedOPT = parseSpaces(chosedOPT)

    try:

        (option, arg) = getopt.getopt(parsedOPT[0:], 'i:t:d:s:')

    except getopt.GetoptError as err:

        print((str(err)))

        sys.exit()

    modifiers = []

    ticket = {}

    for (op, ar) in option:
        if op == '-i':

            id = ar

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

            try:
                checkStatus(status)

                present_status = "status"

                modifiers.append(present_status)

                ticket['status'] = (status)

            except ValueError:

                print(messages.ERR_MSG_STATUS)

                sys.exit()



        elif op == '-d':

            description = str(ar)

            present_description = "description"

            modifiers.append(present_description)

            ticket['description'] = description

    return modifiers , ticket







