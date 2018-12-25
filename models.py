from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os
import sys

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    middle_name = Column(String(80))
    last_name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    phone_number = Column(String(20))
    created_at = Column(DateTime, default=func.now())
    role = Column(Integer)


class Property(Base):
    __tablename__ = 'property'

    id = Column(Integer, primary_key=True)
    address = Column(String(250), nullable=False)
    city = Column(String(80), nullable=False)
    country = Column(String(80), nullable=False)
    rent_price = Column(Integer)
    property_type = Column(String(80))
    description = Column(String(450))
    lat = Column(Integer)
    lng = Column(Integer)
    vacancy = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))


class Bill(Base):
    __tablename__ = 'bill'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    bill_type = Column(String(80))
    description = Column(String(450))
    status = Column(Integer)
    datetime = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('property.id'), nullable=False)
    resident_id = Column(Integer, ForeignKey('resident.id'))


class Resident(Base):
    __tablename__ = 'resident'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    middle_name = Column(String(80))
    last_name = Column(String(80), nullable=False)
    email = Column(String(150), nullable=False)
    phone_number = Column(String(20))
    description = Column(String(450))
    status = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    property_id = Column(Integer, ForeignKey('property.id'))



engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)