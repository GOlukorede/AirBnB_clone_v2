#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type




class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    
    if storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete, delete-orphan')
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals to the current State.id"""
            from models import Storage
            from model.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
            
