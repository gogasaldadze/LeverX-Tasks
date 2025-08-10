from configurator.connection import ConnectionManager
from queries import (
    CountStudentsInRoom,
    LargestAgeDifference,
    SmallestAverageAge,
    StudentDifferentSex,
)


def execute(selected_query):

    db_connection = ConnectionManager().get_connection_with_db("task_3_db")

    analysis_classes = {
        "largest_age_difference": LargestAgeDifference,
        "count_students_in_room": CountStudentsInRoom,
        "smallest_average_age": SmallestAverageAge,
        "different_sex_in_room": StudentDifferentSex,
    }

    if selected_query not in analysis_classes:
        raise NotImplementedError

    query_class = analysis_classes[selected_query]
    query = query_class(db_connection)
    result = query.run()
    for row in result:
        print(row)

    db_connection.close()


if __name__ == "__main__":
    execute()
