#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


metadata = Base.metadata

place_amenity = Table("place_amenity", metadata, Column("place_id",
                                                        String(60),
                                                        ForeignKey(
                                                            "places.id"),
                                                        primary_key=True,
                                                        nullable=False),
                      Column("amenity_id", String(60), ForeignKey(
                                                            "amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)

        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

        name = Column(String(128), nullable=False)

        description = Column(String(1024))

        number_rooms = Column(Integer, nullable=False, default=0)

        number_bathrooms = Column(Integer, nullable=False, default=0)

        max_guest = Column(Integer, nullable=False, default=0)

        price_by_night = Column(Integer, nullable=False, default=0)

        latitude = Column(Float)

        longitude = Column(Float)

        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False,
                                 back_populates="place_amenities")

    else:
        city_id = user_id = name = description = ''
        number_rooms = number_bathrooms = max_guest = price_by_night = 0
        latitude = longitude = 0.0

        @property
        def reviews(self):
            """
            """
            from models.__init__ import storage
            results = storage.all('Review')
            instances = []
            for review in results:
                if review.place_id == self.id:
                    instances.append(review)
            return instances

        @property
        def amenities(self):
            """
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """
            """
            if obj is not None:
                if type(obj).__name__ != 'Amenity':
                    return
                from models.__init__ import storage
                results = storage.all('Amenity')
                for amenity in results:
                    if amenity.place_id == self.id:
                        self.amenity_ids.append(amenity.id)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
