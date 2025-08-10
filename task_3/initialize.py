from configurator.connection import ConnectionManager
from configurator.create_database import CreateDataBase
from schema import RoomSchema, StudentSchema, IndexManager
from data_loader import RoomsDataLoader, StudentDataLoader
from data_inserter import RoomInserter, StudentInserter


def initializer():
    #  Connect WITHOUT database to create database
    raw_connection = ConnectionManager().get_connection()
    print("SQL server connection Established ! ")

    # Database Create
    CreateDataBase(raw_connection, "task_3_db").create()
    raw_connection.close()

    #  Connect WITH database to work with tables and data
    db_connection = ConnectionManager().get_connection_with_db("task_3_db")
    print("Successfully connected to Database")

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

    #  Close the DB connection
    db_connection.close()


if __name__ == "__main__":
    initializer()
