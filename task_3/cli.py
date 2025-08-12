import argparse
import getpass
from initialize import initializer
from queries.executer import execute
from config.env_config import save_to_env, load_config


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
        host = input("Enter MySQL host (default 'localhost'):") or "localhost"
        user = input("Enter MySQL user (default 'root'):") or "root"
        password = getpass.getpass("Enter your MySQL password: ")
        database = input("Enter database name (default 'task_3_db'):") or "task_3_db"

        save_to_env(host, user, password, database)

        return initializer(host, user, password, database)

    elif args.command == "execute":
        config = load_config()
        if config is None:
            print("Config file not found. Please run 'initdb' first.")
            return

        host = config.get("host")
        user = config.get("user")
        password = config.get("password")
        database = config.get("database")

        return execute(args.query_name, host, user, password, database)


if __name__ == "__main__":
    run_cli()
