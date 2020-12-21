from peewee import Model
import peewee

from src.dependency.provider import Container


class BaseModel(Model):
    class Meta:
        database: peewee.Database = Container.db_client