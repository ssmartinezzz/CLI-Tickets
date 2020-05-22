from dbFunctions import *


def filterAction(filters,values):

    tickets = listTicketsbyDateAuthOrStatus()
    if("without"in filters):
        if("pagination" in filters):
            tickets = tickets.slice((values['pagination'] * 6), ((values['pagination'] * 6) + 6))
        else:
            tickets = tickets.slice(1 * 6, (1 * 6) + 6)

    else:
        if ("author" in filters):

            tickets = tickets.filter(Ticket.author == values['author'])

        elif ("date" in filters):

            tickets = tickets.filter(Ticket.date == values['date'])

        elif ("status" in filters):

            tickets = tickets.filter(Ticket.status == values['status'])
        elif ("pagination" in filters):
            tickets = tickets.slice((values['pagination'] * 6), ((values['pagination'] * 6) + 6))
            print("Page doesn't exists!")

        elif not "pagination" in filters:
            tickets = tickets.slice(1 * 6, (1 * 6) + 6)




    result = session.execute(tickets).fetchall()

    return result

def filterExport(filters,values):

    tickets = listTicketsbyDateAuthOrStatus()
    if ("without" in filters):

        tickets = tickets

    else:

        if ("author" in filters):

            tickets = tickets.filter(Ticket.author == values['author'])

        elif ("date" in filters):

            tickets = tickets.filter(Ticket.date == values['date'])

        elif ("status" in filters):

            tickets = tickets.filter(Ticket.status == values['status']
                                     )
    result = session.execute(tickets).fetchall()

    return  result
