from core.database_manager import DBManager
from queries import QueryManager


def execute(selected_query, host, user, password, database):

    db_connection = DBManager(host, user, password).get_connection_with_db(database)

    query_manager = QueryManager(db_connection)

    analysis_methods = {
        "largest_age_difference": query_manager.largest_age_differecne,  # Note: Fix the typo (differecne → difference)
        "count_students_in_room": query_manager.count_students_in_room,
        "smallest_average_age": query_manager.smallest_average_age,
        "different_sex_in_room": query_manager.students_different_sex,
    }

    if selected_query not in analysis_methods:
        raise NotImplementedError

    method = analysis_methods[selected_query]
    result = method()

    for row in result:
        print(row)

    db_connection.close()


if __name__ == "__main__":
    execute()
