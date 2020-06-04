import datetime
import time

from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError


from dbConfiguration import *

from jsonService import *

from models import Ticket


def addTicket(data,lock):



    datetoday = datetime.date.today()

    ticket = Ticket.jsonToTicket(data)

    ticket.date = datetoday

    ticket.status = "pending"

    with lock:
        session.add(ticket)

        try:

            session.commit()

        except SQLAlchemyError as e:

            session.rollback()

            print(e)





def listTicketsbyDateAuthOrStatus():

    query= session.query(Ticket)
    return query


def existsTicket (id):
    if(session.query(exists().where(Ticket.id == id))):
        return True
    else:
        return False

def getTicketbyId(id):

    ticket = session.query(Ticket).get(int(id))


    return ticket.ticketToJson()




def editTicket(id,dataTicket):


    ticketModeable = session.query(Ticket).get(int(id))

    ticketModeable.title = dataTicket['title']

    ticketModeable.description = dataTicket['description']

    ticketModeable.status = dataTicket['status']

    session.add(ticketModeable)

    try:

        session.commit()

    except SQLAlchemyError as e:

        session.rollback()

        print(e)


