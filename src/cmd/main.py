from typing import Optional
from fastapi import FastAPI
from src.dependency.provider import container


from src import config
if __name__ == '__main__':
    app = FastAPI()
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    # container.init_resources()    
    config.setup_config()    