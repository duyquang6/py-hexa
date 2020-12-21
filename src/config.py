from src.dependency.provider import Container

__CONFIG_VARS = [
    "DATABASE_NAME"
]

def setup_config(container: Container):    
    for var in __CONFIG_VARS:
        getattr(container.config, var).from_env(var)