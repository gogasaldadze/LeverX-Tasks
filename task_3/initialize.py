from core.connection import ConnectionManager
from core.create_database import CreateDataBase
from schema import RoomSchema, StudentSchema, IndexManager
from data_loader import RoomsDataLoader, StudentDataLoader
from data_inserter import RoomInserter, StudentInserter
import getpass
import sys
from config.db_config import save_config


def initializer(host, user, password, database):
    #  Connect WITHOUT database to create database
    raw_connection = ConnectionManager(host, user, password).get_connection()
    print("SQL server connection Established ! ")

    # Database Create
    CreateDataBase(raw_connection, database).create()
    raw_connection.close()

    #  Connect WITH database to work with tables and data
    db_connection = ConnectionManager(host, user, password).get_connection_with_db(
        database
    )
    print(f"Successfully connected to {database}")

    #  Create tables
    with RoomSchema(db_connection) as room_schema:
        room_schema.create()
        print("rooms Table Created ! ")
    with StudentSchema(db_connection) as student_schema:
        student_schema.create()
        print("students Table Created ! ")

    #  Create Indexes
    with IndexManager(db_connection) as index:
        index.create()

    #  Load data
    rooms = RoomsDataLoader().load()
    students = StudentDataLoader().load()

    #  Insert data
    with RoomInserter(db_connection) as room_inserter:
        room_inserter.insert(rooms)
    with StudentInserter(db_connection) as student_inserter:
        student_inserter.insert(students)

    # save config
    save_config(host, user, password, database)

    #  Close the DB connection
    db_connection.close()
