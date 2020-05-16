import datetime


from sqlalchemy.exc import SQLAlchemyError

from dbConfiguration import *

import threading
from jsonService import *
from models import Ticket


def addTicket(socket,lock):

    lock.acquire()

    ticketrecv = recvJson(socket)

    print(ticketrecv)

    datetoday = datetime.date.today()

    ticket = Ticket.jsonToTicket(ticketrecv)

    ticket.date = datetoday

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
        .filter((Ticket.author ==['author'])|(Ticket.date == ['date']) |(Ticket.status == ['status']))






