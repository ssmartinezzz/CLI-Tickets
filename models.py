from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from dbConfiguration import Base


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    title = Column(String(45))
    author = Column(String(45))
    description = Column(String(300))
    status = Column(String(20))
    date = Column(Date)

    def __repr__(self):
        """
        Pyhton getter of Ticket
        @return: returns a ticket with its attributes
        """
        return'<Ticket: %r %r %r %r %r %r  >' % (self.id, self.title, self.author, self.description, self.status, self.date)

    def __init__(self, title, author, description, status, date):
        """
        Constructor of a Ticket object
        @param title: its a string with size up to 45 characters
        @param author: its a string with size up to 45 characters
        @param description: its a string with size up to 300 characters
        @param status: its a string with size up to 20 characters
        @param date: its Date type column
        """
        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date


    def ticketToJson(self):
        """
        Function that converts an instance of Ticket to a JSON format.
        @return: returns a specific ticket in json format.
        """
        ticketjson = {
            'id':self.id,
            'title': self.title,
            'author': self.author,
            'date': str(self.date),
            'description': self.description,
            'status': self.status

        }
        return ticketjson


    @staticmethod
    def jsonToTicket(ticketjson):
        """
        converts values from a json to a Ticket object
        @param ticketjson: a json object that contains keys and values
        of a Ticket. e.g "title","Lake Ness"
        @return: returns a Ticket object
        """
        title = ticketjson.get('title')
        author = ticketjson.get('author')
        description = ticketjson.get('description')
        status = ticketjson.get('status')
        date = ticketjson.get('date')
        return Ticket(title=title,author=author,description=description,status=status,date=date)


Base.metadata.create_all()
