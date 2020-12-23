from src.dependency.provider import Container
from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    @dataclass
    class Database:
        name: str = ('DATABASE_NAME', 'haha')

    database: Database = Database()
    port: int = 'APP_PORT'


def setup_config():
    app_config = AppConfig()

    def _setup(config):
        for key, value in vars(config).items():
            if isinstance(value, (str, int, float)):
                setattr(config, key, os.getenv(value))
            elif isinstance(value, tuple):
                val = os.getenv(value[0]) or value[1]
                setattr(config, key, val)
            else:
                _setup(value)
    _setup(app_config)
    print(app_config)
