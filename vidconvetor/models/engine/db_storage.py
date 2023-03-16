import models
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None


    def __init__(self):
        """Instantiate a DBStorage object"""
        VICO_MYSQL_USER = getenv('VICO_MYSQL_USER')
        VICO_MYSQL_PWD = getenv('VICO_MYSQL_PWD')
        VICO_MYSQL_HOST = getenv('VICO_MYSQL_HOST')
        VICO_MYSQL_DB = getenv('VICO_MYSQL_DB')
        self.__engine = create_engine(f"mysql+mysqldb://{VICO_MYSQL_USER}:{VICO_MYSQL_PWD}@{VICO_MYSQL_HOST}/{VICO_MYSQL_DB}")
        
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self, obj):
        """commit all changes of the current database session"""
        self.__session.commit()

