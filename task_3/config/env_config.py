import os
from dotenv import load_dotenv


def save_to_env(host, user, password, database, filename=".env"):
    with open(filename, "w") as f:
        f.write(f"DB_HOST={host}\n")
        f.write(f"DB_USER={user}\n")
        f.write(f"DB_PASSWORD={password}\n")
        f.write(f"DB_NAME={database}\n")


def load_config(env_path=".env"):
    load_dotenv(env_path)

    config = {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
    }

    if not all(config.values()):
        print(
            f"Missing database configuration in {env_path}. Please run 'initdb' first."
        )
        return None

    return config
