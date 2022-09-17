#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv
import models


""" place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id',
           String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False)
    ) """


class Place(BaseModel, Base):
    """This is the class for Place """
    __tablename__ = 'places'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False, backref='places')

        place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column('place_id',
                   String(60),
                   ForeignKey('places.id'),
                   primary_key=True,
                   nullable=False),
            Column('amenity_id',
                   String(60),
                   ForeignKey('amenities.id'),
                   primary_key=True,
                   nullable=False)
        )

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ getter reviews """
            from models import storage
            ret = []
            dict = storage.all(Review)
            for k, v in dict.items():
                if self.id == v["place_id"]:
                    ret.append(v)
            return ret

        @property
        def amenities(self):
            """ getter amenities """
            from models import storage
            from models.amenity import Amenity
            ret = []
            for k, v in storage.all(Amenity).items():
                ret.append(v)
            return ret

        @amenities.setter
        def amenities(self, value):
            """ setter Smenities """
            from models import storage
            from models.amenity import Amenity
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
