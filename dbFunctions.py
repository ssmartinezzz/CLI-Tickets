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
    ticket = Ticket(title=ticketrecv['title'],author=ticketrecv['author'],description=ticketrecv['description'],status="pending",date=datetoday)

    session.add(ticket)

    try:

        session.commit()

    except SQLAlchemyError as e:

        session.rollback()

        print(e)

    lock.release()