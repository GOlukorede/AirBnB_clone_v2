#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Accessing the environment variables
env = os.getenv('HBNB_ENV', 'dev')
mysql_user = os.getenv('HBNB_MYSQL_USER')
mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
mysql_host = os.getenv('HBNB_MYSQL_HOST')
mysql_db = os.getenv('HBNB_MYSQL_DB')
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')

# Initialize storage based on the storage type
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()