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


# From here goes all user requests
@app.get('/user/auth/{uuid}/info')
async def get_user_info(uuid: str):
    return "Working"


@app.post('/user/auth')
async def auth_user():
    ...
