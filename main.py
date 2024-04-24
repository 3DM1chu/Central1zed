from typing import Union, Annotated
from fastapi import FastAPI, Header
import orjson as json

from auth import AuthorizationStorage
from client import Client

app = FastAPI()
auth = AuthorizationStorage()


@app.get("/")
async def getClients():
    return auth.clients


@app.post("/")
async def addClient(client: Client, API_TOKEN: Annotated[str | None, Header()] = None):
    auth.authorizeNewClient(client)
    return {"clients": auth.clients, "API_TOKEN": API_TOKEN}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    """
    Open your browser at http://127.0.0.1:8000/items/5?q=somequery.
    {"item_id": 5, "q": "somequery"}
    :param item_id:
    :param q:
    :return:
    """
    return {"item_id": item_id, "q": q}
