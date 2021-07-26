from typing import Optional
from fastapi import FastAPI, Response, Cookie
# from pulsar import Client

app = FastAPI()
# client = Client('pulsar://localhost:6650')
# consumer = client.subscribe('topic', subscription_name='reused_subscription')

@app.get("/")
def root(response: Response, sesh_token: Optional[str] = Cookie(None)):
    if sesh_token is None: 
        response.set_cookie(key="sesh_token", value="sesh-value")

    return {"Hello":sesh_token}