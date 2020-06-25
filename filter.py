from dbFunctions import *
import messages

def filter_action(filters, values):
    """
    Functions that depending on the filters applied by the client would
    filter the query of all tickets and return a list of them paginated.
    Size(0-6)
    @param filters: array that contains the name of the filters applied by the client
    @param values: values of the different filters that are going to be applied.
    @return: returns a list containing the results of the application of filters.
    """
    tickets = list_tickets()

    if"without"in filters:

        if"pagination" in filters:

            tickets = tickets.slice((values['pagination'] * 6), ((values['pagination'] * 6) + 6))

        else:

            tickets = tickets.slice(0 , 6)

    else:

        if "author" in filters:

            tickets = tickets.filter(Ticket.author == values['author'])

        if "date" in filters:

            tickets = tickets.filter(Ticket.date == values['date'])

        if "status" in filters:

            tickets = tickets.filter(Ticket.status == values['status'])

        pag = 0

        if "pagination" in filters:

            pag = values['pagination']

        tickets = tickets.slice((pag * 6), ((pag* 6) + 6))

    tickets_list = list()

    result = tickets.all()

    if not result:

        tickets_list.append(messages.ERR_MSG_NOAVAILABLE)

    else:

        for ticket in result:
        
            tickets_list.append(ticket.ticketToJson())

    return tickets_list

def edition_filter(id, modifiers, dataTicket):
    """
    Function that implents Boolean Algebra for implementing simultaneous edition of a Ticket

    @param id: Identificator of the Ticket that is going to be edited.
    @param modifiers: Array that contains the name of the modifiers that are going to be applied on the Ticket.
    @param dataTicket: Values of the different modifiers
    @return: returns an Array containing the changes in a Ticket
    """
    ticket_modeable = session.query(Ticket).get(int(id))

    local_attributes = [ticket_modeable.title, ticket_modeable.description, ticket_modeable.status]

    if "title" in modifiers and "description" in modifiers and "status" in modifiers:

        local_attributes[0] = dataTicket['title']

        local_attributes[1] = dataTicket['description']

        local_attributes[2] = dataTicket['status']

    elif "title" in modifiers and "description" in modifiers:

        local_attributes[0] = dataTicket['title']

        local_attributes[1] = dataTicket['description']

    elif "title" in modifiers and "status" in modifiers:

        local_attributes[0] = dataTicket['title']

        local_attributes[2] = dataTicket['status']

    elif "title" in modifiers:

        local_attributes[0] = dataTicket['title']

    elif "description" in modifiers and "status" in modifiers:

        local_attributes[1] = dataTicket['description']

        local_attributes[2] = dataTicket['status']

    elif "description" in modifiers:

        local_attributes[0] = dataTicket['description']

    elif "status" in modifiers:

        local_attributes[2] = dataTicket['status']

    return local_attributes


