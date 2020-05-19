import datetime

from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError


from dbConfiguration import *

from jsonService import *

from models import Ticket


def addTicket(socket,lock):

    lock.acquire()

    ticketrecv = recvJson(socket)

    print(ticketrecv)

    datetoday = datetime.date.today()

    ticket = Ticket.jsonToTicket(ticketrecv)

    ticket.date = datetoday

    ticket.status = "pending"

    session.add(ticket)

    try:

        session.commit()

    except SQLAlchemyError as e:

        session.rollback()

        print(e)

    lock.release()

def listTicketsbyDateAuthOrStatus(socket):

    kwargs = recvJson(socket)

    return session.query(Ticket)  \
        .filter((Ticket.author == kwargs['author']) and (Ticket.date == kwargs['date']) and (Ticket.status == kwargs['status']))



def existsTicket (id):
    return session.query(exists().where(Ticket.id == id)).scalar()

def getTicketbyId(id):

    ticket = session.query(Ticket).get(int(id))

    return ticket.ticketToJson()




def editTicket(data,lock):

    lock.acquire()

    ticketModeable = session.query(Ticket).get(int(data['id']))

    ticketModeable.title = data['title']

    ticketModeable.author = data['author']

    ticketModeable.description = data['description']

    ticketModeable.status = data['status']

    ticketModeable.date = datetime.date.today()

    session.add(ticketModeable)

    try:

        session.commit()

    except SQLAlchemyError as e:

        session.rollback()

        print(e)

    lock.release()

