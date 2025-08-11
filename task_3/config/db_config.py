import os
import json


def save_config(
    host, user, password, database, folder="config", filename="db_config.json"
):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    config = {
        "host": host,
        "user": user,
        "password": password,
        "database": database,
    }
    with open(path, "w") as f:
        json.dump(config, f)
    print(f"Connection info saved to {path}")


def load_config(folder="", filename="db_config.json"):
    import os

    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, folder, filename)

    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found at {path}. Please run 'initdb' first.")
        return None
