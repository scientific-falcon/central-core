from fastapi import FastAPI
from env2 import env2 as env


app = FastAPI(debug=bool(env('APP_LEVEL', False, False)))


@app.get('/')
async def index():
    """
    Index page

    Just exists, to show possibilities of this project
    """
    return "Hello, world"
