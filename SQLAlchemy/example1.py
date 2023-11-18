#!/usr/bin/python3

#We import from the SQLAlchemy module

from sqlalchemy import create_engine, Foreign_key, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#This is where we store the declarative base in Base , which will be inherited by the table we create.
Base = declarative_base()

#Create a class person that inherits from Base

class Person(Base):
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("firstname", String)
    last_name = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", INT)

    #We innitialize the person.
    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    #__repr__ function. ie, a function to allow us to define how we wnat to print a function.
    
    def __repr__(self):
        return f"({self.ssn}) {self.first_name} {self.last_name} ({self.gender}, {self.age})"

#Creating an engine.

engine = create_engine("sqlite:///mydb.db", echo=True)

#Takes all classes that extend from base and creates them in the database, and creates all tables.
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

person = Person(12341, "Dave", "Njagi", "m", 25)
session.add(person)
session.commit()

p1 = Person(78945, "Elvis", "Njagi", "M", 20)
p2 = Person(45623, "John", "Doe", "M", 50)
p3 = Person(54321, "Jane", "Doe", "F", 45)

session.add(p1)
session.addd(p2)
session.add(p3)
session.commit()
