#
# import os
#
# class Config:
#     SQLALCHEMY_DATABASE_URI = os.environ.get(
#         "DATABASE_URL",              # Docker / Kubernetes
#         "sqlite:///instance/massage.db"  # локално без Docker
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
import os

class Config:

    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
        db_host = os.environ.get("DB_HOST")
        db_name = os.environ.get("DB_NAME")
        if db_user and db_password and db_host and db_name:
            database_url = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}"
        else:
            database_url = "sqlite:///instance/massage.db"

    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
