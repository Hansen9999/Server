from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from api import Base

class Customer(Base):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @declared_attr
    def __tablename__(self):
        return 'customer'

    # username, max length 64
    name = Column(String(64), primary_key=True)
    password = Column(String(64))

