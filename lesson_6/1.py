@app.post('/users/', response_model=User)
async def create_user(new_user: UserIn):
    users.append(User(id=len(users) + 1,
                      name=new_user.name,
                      email=new_user.email,
                      password=new_user.password))

    return users[-1]


@app.get('/users/', response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put('/users/', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    try:
        current_user = users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail='user not found')
    else:
        current_user.name = new_user.name
        current_user.email = new_user.email
        current_user.password = new_user.password

    return current_user


@app.delete('/users/', response_model=dict)
async def delete_user(user_id: int):
    try:
        del users[user_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail='Task not found')
    return {"message": 'Успешно удален'}


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
