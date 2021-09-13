from sqlalchemy import Column, String, Date

from src.models.base import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    name = Column(String)
    realName = Column(String)
    crtnDate = Column(Date)
    chgDate = Column(Date)

    def __init__(self, id, name, realName, crtnDate, chgDate):
        self.id = id
        self.name = name
        self.realName = realName
        self.crtnDate = crtnDate
        self.chgDate = chgDate
    
    def __repr__(self):
        return f"<User({self.id}, {self.name}, {self.realName}, {self.crtnDate}, {self.chgDate})>"