from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import *

DB_NAME="MyDatabaseName"
engine=create_engine('mysql+pymysql://root:@localhost/{}'.format(DB_NAME),echo=False)
Base=declarative_base()
session=Session(bind=engine)

class post(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    title=Column(String(50))
    body=Column(String(50))
    def __repr__(self):
        return "<Post(id={},title={},body={}>".format(self.id,self.title,self.body)



