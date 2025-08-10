import argparse
from initialize import initializer
from executer import execute


def run_cli():
    analysis_classes = {
        "largest_age_difference",
        "count_students_in_room",
        "smallest_average_age",
        "different_sex_in_room",
    }

    parser = argparse.ArgumentParser(description="Manage database operations")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("initdb", help="Initialize the database")

    runqueries_parser = subparsers.add_parser("execute", help="Run specific query")
    runqueries_parser.add_argument(
        "query_name",
        choices=analysis_classes,
        help="Name of the query to run",
    )

    args = parser.parse_args()

    if args.command == "initdb":
        return initializer()
    elif args.command == "execute":
        return execute(args.query_name)


if __name__ == "__main__":
    run_cli()
