import getopt
import sys
import time
from parserUtilities import *
from utils import *

def mainClientCLI():
    """
    main Cli function that displays the options available for operating
    with the system. This function asks for an option, it parses the
    input-inserted string and it uses on the getopt recognition.

    The correct options for this function are --insert | --list | --edit
    | --export | --exit | --clear
    obviously, if they've short options, they're going to be recognized too.

    @return: it returns the value of the chosed option called "destination".
    That value is used in the future by other functions in the client as in the server.

    """
    print(messages.CLIENT_MENU)

    choosedOption = input("Option ")

    parsedOption = parse_spaces(choosedOption)

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
    """
    function that is implemented when the client selects the 'insert' option
    This function ask for the different required values for inserting
    a new ticket, such as Title, Author and Description.
    When these values are inserted, the result string is parsed, and
    the getopt.getopt method tries to identify that options and values
    
    The values are appended to an array named ticket.
    
    @return: It returns the ticket array which contains the values of a new Ticket.
    These values are going to be sent to the server, who is in charge of uploading ticket
    to the db.
    """
    ticket = []

    chosedOPT = input("command: ")

    parsedOPT = parse_spaces(chosedOPT)

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

def filteredCLI():
    """
    Function that recognizes the values entered, that are going to be applied
    when the client list or export a group of Tickets.

    This function asks for options like "pagination", "author","description"
    "status" or "all"
    These options and values are saved in one string, which is going to be parsed by parseSpaces()
    and reconized by getopt()

    As the filter could be applied simultaneously, the function will save the name of the filters applied in
    an array, but the ticket values are going to be save for now in a dictionary.

    @return:(This function will return 2 things: First, an array with the applied filters and
    second, a dictionary with the values that are going to be applied in the filter.)
    """
    chosed_opt = input("command:")

    parsed_opt = parse_spaces(chosed_opt)

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
                searchDate = date_format(date)

                present_date = "date"

                filters_applied.append(present_date)

                ticket['date'] = searchDate

            except ValueError:

                print(messages.ERR_MSG_DATE)

                sys.exit()

        elif op == '-s':

            status =str(ar)

            try:
                check_status(status)

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
    """
    unction that recognizes the values entered, that are going to be applied
    when the client edit one Ticket.

    This function asks for options like "author", "Title","description"
    "status" or "Id"
    The most important value to specify is the id.
    These options and values are saved in one string, which is going to be parsed by parseSpaces()
    and reconized by getopt()

    Options are saved in modifiers (Array) and arguments are saved in ticket (Dictionary)

    @return: This function returns the modifiers applied to a specific ticked and
    also returns their values saved in ticket.
    """
    chosedOPT = input("command: ")

    parsedOPT = parse_spaces(chosedOPT)

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
                check_status(status)

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

    return modifiers, ticket







