#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    else:
        name = ''
        @property
        def cities(self):
            from models.__init__ import storage
            cts = []
            results = storage.all('City')
            for city in results:
                if city.state_id == self.id:
                    cts.append(city)
            return cts
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
