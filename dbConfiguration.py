import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

dbUrl = 'mysql+pymysql://'+os.getenv('DB_USERNAME')+':'+os.getenv('DB_PASS')+'@localhost/tickets'


engine = create_engine(dbUrl)

Session = sessionmaker(bind=engine)

Base = declarative_base(bind=engine)

session = Session()
