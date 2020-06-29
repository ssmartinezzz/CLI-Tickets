import datetime
import time
from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError
from dbConfiguration import *
from jsonService import *
from models import Ticket

def add_ticket(data, lock):
    """
    Function that recives values of a ticket trough a socket (Server)
    and creates a new Ticket() object and set its attributes.
    Some attributes are set manually by this function like "date" and
    "status" but the others come from the socket.
    @param data: (Contains in a JSON format values of a ticket such as Title, Author and Description.)
    @param lock:  (threading.Lock() implementation that implements mutex)
    """
    today = datetime.date.today()

    ticket = Ticket.jsonToTicket(data)

    ticket.date = today

    ticket.status = "pending"

    with lock:

        session.add(ticket)

        try:

            session.commit()

        except SQLAlchemyError as e:

            session.rollback()

            print(e)

def list_tickets():
    """
    function that search all the tickets available in the DataBase.
    @return: The query statement for all the tickets in the db.
    """
    query = session.query(Ticket)

    return query


def exists_ticket(id):
    """
    Function that verifies if a Ticket exists on the Database
    @param id: (Int value given by a client that represents the Ticket's ID which is going to be verified.)
    @return: It returns a boolean value True or False depending on the existence of the Ticket.
    """
    try:

        result = session.query(Ticket).get(int(id))

        if result is not None:

            val = True

        else:

            val = False
            
    except ValueError:
        
        val = False

    return val

def getticketbyid(id):
    """
    It gets from the database the Ticket object with the given ID.
    @param id: represents the ID of the Ticket.
    @return:Returns the Ticket object converted to a Json object 
    so the server socket can send it. 
    """
    ticket = session.query(Ticket).get(int(id))

    return ticket.ticketToJson()

def edit_ticket(id, params_applied):
    """
    Function that edits the given ticket ID with the given applied parameters
    @param id: Ticket Identificator that represents the ticket that is going to be edited 
    @param params_applied: Modifications did on the Ticket, if a value wasn't changed
    it would be replace as well but with the same existing value. 
    """
    ticket_modeable = session.query(Ticket).get(int(id))

    "If only one attribute is modified in params_applied we'll have the first values of the ticket"
    ticket_modeable.title = params_applied[0]

    ticket_modeable.description = params_applied[1]

    ticket_modeable.status = params_applied[2]

    session.add(ticket_modeable)

    try:

        session.commit()

    except SQLAlchemyError as e:

        session.rollback()

        print(e)


