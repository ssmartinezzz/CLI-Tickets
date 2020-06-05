from dbFunctions import *

def filterAction(filters,values):

    tickets = listTicketsbyDateAuthOrStatus()

    if"without"in filters:

        if"pagination" in filters:

            tickets = tickets.slice((values['pagination'] * 6), ((values['pagination'] * 6) + 6))

        else:

            tickets = tickets.slice(1 * 6, (1 * 6) + 6)

    else:

        if "author" in filters:

            tickets = tickets.filter(Ticket.author == values['author'])

        elif "date" in filters:

            tickets = tickets.filter(Ticket.date == values['date'])

        elif "status" in filters:

            tickets = tickets.filter(Ticket.status == values['status'])

        elif "pagination" in filters:

            tickets = tickets.slice((values['pagination'] * 6), ((values['pagination'] * 6) + 6))

        elif "pagination" not in filters:

            tickets = tickets.slice(1 * 6, (1 * 6) + 6)

    array = list()

    result = tickets.all()

    for ticket in result:

        array.append(ticket.ticketToJson())

    return array

def editionFiltred(id,modifiers,dataTicket):

    ticketModeable = session.query(Ticket).get(int(id))

    local_attributes = []
    local_attributes.append(ticketModeable.title)
    local_attributes.append(ticketModeable.description)
    local_attributes.append(ticketModeable.status)

    print(local_attributes)

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


