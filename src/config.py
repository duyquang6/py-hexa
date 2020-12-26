from src.dependency.provider import Container
from dataclasses import dataclass
import os


@dataclass
class AppConfig:
    @dataclass
    class Database:
        name: str = ('DATABASE_NAME')

    database: Database = Database()


def setup_config():
    app_config = AppConfig()

    def _setup(config):
        for key, value in vars(config).items():
            if isinstance(value, (str, int, float, bool)):
                env_cls = config.__annotations__[key]
                value = os.getenv(value)
                if env_cls == bool:
                    if str(value).lower() not in ('true', '1'):
                        value = False
                    else:
                        value = True
                if value is None:
                    setattr(config, key, None)
                else:
                    setattr(config, key, env_cls(value))
            elif isinstance(value, tuple):
                env_cls = config.__annotations__[key]
                val = None
                if len(value) == 1:
                    val = os.getenv(value[0])
                if len(value) == 2:
                    val = os.getenv(value[0]) or value[1]
                if env_cls == bool:
                    if str(val).lower() not in ('true', '1'):
                        val = False
                    else:
                        val = True
                if val is None:
                    setattr(config, key, None)
                else:
                    setattr(config, key, env_cls(val))
            else:
                _setup(value)
    _setup(app_config)
    return app_config
