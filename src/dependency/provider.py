import inject
from fastapi import FastAPI
from src.dependency.db_connector import DatabaseInterface, SQLiteAdapter
import os
from src import config



def configure_application(app: FastAPI) -> None:
    app.config.update(
        DATABASE_URI=config.settings.database_uri
    )

def configure_inject(app: FastAPI) -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(DatabaseInterface, SQLiteAdapter(app.config['DATABASE_URI']))

    inject.configure(config)

