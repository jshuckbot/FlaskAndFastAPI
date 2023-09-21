from fastapi import APIRouter, HTTPException
from db import users, database

from models.user import User, UserIn

router = APIRouter()


@router.get('/fake_users/{count}')
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(first_name=f'first_name{i}',
                                      last_name=f'last_name{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.post('/users/', response_model=UserIn)
async def create_user(user: UserIn):
    query = users.insert().values(first_name=user.first_name,
                                  last_name=user.last_name,
                                  email=user.email,
                                  password=user.password)
    await database.execute(query)
    return user


@router.get('/users/', response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.put('/users/{user_id}', response_model=UserIn)
async def upload_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@router.delete('/users/{uder_id}', response_model=dict)
async def delete_users(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
