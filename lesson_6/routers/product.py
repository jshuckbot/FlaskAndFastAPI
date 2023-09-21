from fastapi import APIRouter, HTTPException
from db import products, database

from models.product import Product, ProductIn

router = APIRouter()


@router.get('/fake_products/{count}')
async def create_note_products(count: int):
    for i in range(count):
        query = products.insert().values(name=f'name_product{i}',
                                         description=f'description{i}',
                                         price=(i + 1) * 100,
                                         is_stock=True)
        await database.execute(query)
    return {'message': f'{count} fake products create'}


@router.post('/products/', response_model=ProductIn)
async def create_product(product: ProductIn):
    query = products.insert().values(name=product.name,
                                     description=product.description,
                                     price=product.price,
                                     is_stock=product.is_stock)
    await database.execute(query)
    return product


@router.get('/products/', response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.put('/products/{product_id}', response_model=ProductIn)
async def upload_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.dict())
    await database.execute(query)
    return {**new_product.dict(), "id": product_id}


@router.delete('/products/{product_id}', response_model=dict)
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}
