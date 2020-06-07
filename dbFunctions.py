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




def editTicket(id,params_applied):

    ticketModeable = session.query(Ticket).get(int(id))

    ticketModeable.title = params_applied[0]

    ticketModeable.description = params_applied[1]

    ticketModeable.status = params_applied[2]

    session.add(ticketModeable)

    try:

        session.commit()

    except SQLAlchemyError as e:

        session.rollback()

        print(e)


