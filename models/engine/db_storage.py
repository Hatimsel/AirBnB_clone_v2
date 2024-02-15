#!/usr/bin/python3
"""
Db Storage
"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """
    DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiates the class
        """
        usr = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(usr, pwd, host, db), pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        """
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        dic = {}
        if cls is not None:
            results = self.__session.query(cls).all()

            for row in results:
                key = str(cls) + '.' + row.id
                dic[key] = row
        else:
            classes = [
                State, City, User
            ]
            for clss in classes:
                results = self.__session.query(clss).all()
                for row in results:
                    if '_sa_instance_state' in row.__dict__.keys():
                        del row.__dict__['_sa_instance_state']
                    cls_name = clss.__dict__['__doc__'].split(' ')[1]
                    key = cls_name + '.' + row.id
                    dic[key] = row
        self.__session.close()
        return dic

    def new(self, obj):
        """
        Adds the obj to the current database Session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session obj
        if not None
        """
        if obj is not None:
            self.__session.delete(obj)

        return

    def reload(self):
        """
        Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        self.reload()
        self.__session.remove()
