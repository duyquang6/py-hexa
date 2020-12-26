from dependency_injector.wiring import Provide
from src.dependency.provider import Container, container
from typing import Optional

app = container.app()


@app.get("/todolist/")
async def create_todo_list(q: Optional[str] = None):
    return {'message': 'OK'}
