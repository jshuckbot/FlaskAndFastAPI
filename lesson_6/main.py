import uvicorn
from fastapi import FastAPI, HTTPException, Request

from db import database
from lesson_6.routers import user, product, order

app = FastAPI()


# templates = Jinja2Templates(directory="templates")


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=['users'])
app.include_router(product.router, tags=['products'])
app.include_router(order.router, tags=['orders'])

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
