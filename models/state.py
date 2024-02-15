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
            from models.city import City
            cts = []
            results = storage.all(City)
            print(results)
            for city in results:
                if results[city].state_id == self.id:
                    del results[city]._sa_instance_state
                    cts.append(results[city])
            return cts
