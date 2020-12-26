from typing import Optional
from src.dependency.provider import container
from src.handler import todolist

from src import config
if __name__ == '__main__':
    container.init_resources()
    config.setup_config()

app = container.app()
@app.get("/")
def read_root():
    return {"Hello": "World"}
