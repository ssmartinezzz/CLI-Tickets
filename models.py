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
        return'<Ticket: %r %r %r %r %r %r  >' % (self.id, self.title, self.author, self.description, self.status, self.date)

    def __init__(self, title, author, description, status, date):
        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date


    def ticketToJson(self):
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
        title = ticketjson.get('title')
        author = ticketjson.get('author')
        description = ticketjson.get('description')
        status = ticketjson.get('status')
        date = ticketjson.get('date')
        return Ticket(title=title,author=author,description=description,status=status,date=date)


Base.metadata.create_all()
