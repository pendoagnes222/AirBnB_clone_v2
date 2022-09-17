#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    """This class defines a reviws atributes"""
    __tablename__ = "reviews"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
