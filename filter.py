from dbFunctions import *


def filterAction(filters,values):

    tickets = listTicketsbyDateAuthOrStatus()

    if ("author" in filters):

        tickets = tickets.filter( Ticket.author == values['author'])

    elif("date"in filters):

       tickets = tickets.filter(Ticket.date == values['date'])

    elif("status" in filters):

        tickets = tickets.filter(Ticket.status == values['status'])

    result = session.execute(tickets)

    return result.fetchall()