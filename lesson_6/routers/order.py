from datetime import datetime
from random import randint

from fastapi import APIRouter, HTTPException
from db import orders, database

from models.order import Order, OrderIn

router = APIRouter()


@router.get('/fake_orders/{count}')
async def create_note_orders(count: int):
    for i in range(count):
        query = orders.insert().values(user_id=randint(1, count),
                                       product_id=randint(1, count),
                                       date=datetime.now(),
                                       status=True)
        await database.execute(query)
    return {'message': f'{count} fake orders create'}


@router.post('/orders/', response_model=OrderIn)
async def create_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id,
                                   product_id=order.product_id,
                                   date=order.date,
                                   status=order.status)
    await database.execute(query)
    return order


@router.get('/oders/', response_model=list[OrderIn])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.put('/oders/{order_id}', response_model=OrderIn)
async def upload_order(order_id: int, new_product: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": order_id}


@router.delete('/orders/{order_id}', response_model=dict)
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}
