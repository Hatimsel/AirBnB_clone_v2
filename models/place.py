#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    name = Column(String(128), nullable=False)

    description = Column(String(1024))

    number_rooms = Column(Integer, nullable=False, default=0)

    number_bathrooms = Column(Integer, nullable=False, default=0)

    max_guest = Column(Integer, nullable=False, default=0)

    price_by_night = Column(Integer, nullable=False, default=0)

    latitude = Column(Float, nullable=False)

    longitude = Column(Float, nullable=False)

    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models.__init__ import storage
            cts = []
            dic = storage.all('City')
            for city_id in dic:
                if dic[city_id].place_id == self.id:
                    results.append(dic[city_id])
            return results


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
