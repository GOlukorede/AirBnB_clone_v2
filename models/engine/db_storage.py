#!/usr/bin/python3
"""DBStorage engine for HBNB project"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """DBStorage engine for HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV', 'dev')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db}',
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_list = [User, State, City, Amenity, Place, Review]
        objects = {}
        
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = f'{type(obj).__name__}.{obj.id}'
                objects[key] = obj
        else:
            for cls in class_list:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = f'{type(obj).__name__}.{obj.id}'
                    objects[key] = obj
        
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
