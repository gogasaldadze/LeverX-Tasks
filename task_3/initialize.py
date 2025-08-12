from core.database_manager import DBManager
from tables.table_manager import TableManager
from data.data_loader import DataLoader
from data.data_inserter import DataInserter


def prepare_database(host, user, password, database):
    db_manager = DBManager(host, user, password)

    db_manager.create_database(database)
    print(f"{database} successfully created")

    connection = db_manager.get_connection_with_db(database)
    print(f"Successfully connected to {database}")
    return connection


def setup_tables(connection):

    with TableManager(connection) as table_manager:
        table_manager.create_all()
        print("All tables and indexes created!")


def load_and_insert_data(connection):

    loader = DataLoader()
    rooms = loader.load_rooms()
    students = loader.load_students()

    with DataInserter(connection) as inserter:
        inserter.insert_rooms_data(rooms)
        inserter.insert_students_data(students)
    print("Initial data inserted!")


def initializer(host, user, password, database):
    """whole database setup process"""
    connection = prepare_database(host, user, password, database)
    setup_tables(connection)
    load_and_insert_data(connection)

    connection.close()
