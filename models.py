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


    def __init__(self,title,author,description,status,date):
        self.title = title
        self.author = author
        self.description = description
        self.status = status
        self.date = date

Base.metadata.create_all()
