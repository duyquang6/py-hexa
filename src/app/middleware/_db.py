from src.cmd import app


# def database_middleware(db: DatabaseInterface):
    
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    database.connect()
    response = await call_next(request)
    database.close()
    return response
