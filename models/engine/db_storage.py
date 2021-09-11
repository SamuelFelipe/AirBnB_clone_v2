#!/usr/bin/python3

'''
Class to manage the database
'''

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''Class to manage the storage in a database'''
    __engine = None
    __session = None

    classes = {
               'User': User, 'Place': Place,
               'State': State, 'City': City,
               'Amenity': Amenity,
               'Review': Review
              }

    def __init__(self):
        '''Cretate a new session'''
        crt = {
            "user": getenv("HBNB_MYSQL_USER"),
            "pwd": getenv("HBNB_MYSQL_PWD"),
            "host": getenv("HBNB_MYSQL_HOST"),
            "db": getenv("HBNB_MYSQL_DB")
        }
        f = 'mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}'.format(**crt)
        self.__engine = create_engine(f, encoding='utf-8', pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def new(self, obj):
        '''Create a new object instance'''
        self.__session.add(obj)

    def all(self, cls=None):
        '''list all the entries of a class if one is pased
            otherwise list all the elementes in the db
        '''
        objs = {}
        if cls:
            my_query = self.__session.query(self.classes[cls]).all()
            for obj in my_query:
                objs[cls + "." + obj.id] = obj
        else:
            for key, value in self.classes.items():
                my_query = self.__session.query(value).all()
                for obj in my_query:
                    objs[key + "." + obj.id] = obj

        return objs

    def save(self):
        '''Commit the changes'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Remove a instance if it exist'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Reload all the items in stored in the db'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''finalize the session'''
        self.__session.remone()
