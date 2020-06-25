from dbFunctions import *

def filterAction(filters,values):

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

    array = list()

    result = tickets.all()

    for ticket in result:

        array.append(ticket.ticketToJson())

    return array

def editionFiltred(id,modifiers,dataTicket):

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


