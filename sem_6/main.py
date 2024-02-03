from fastapi import FastAPI
from typing import List
from models import User, Item, Order, UserIn, ItemIn, OrderIn
from database import users_db, items_db, orders_db, database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello !!"}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users_db.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users_db.select().where(users_db.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    new_user = users_db.insert().values(**user.model_dump())
    new_id = await database.execute(new_user)
    return {**user.model_dump(), 'id': new_id}


@app.put("//users/{user_id}")
async def update_user(user_id: int, new_user: UserIn):
    query = users_db.updata().where(users_db.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {'message': 'User updated'}


@app.delete("/users/{users_id}")
async def delete_user(user_id: int):
    query = users_db.delete().where(users_db.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.get("/items/", response_model=List[Item])
async def read_items():
    query = items_db.select()
    return await database.fetch_all(query)


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items_db.select().where(items_db.c.id == item_id)
    return await database.fetch_one(query)


@app.post("/items/", response_model=Item)
async def create_item(item: ItemIn):
    new_item = items_db.insert().values(**item.model_dump())
    new_id = await database.execute(new_item)
    return {**item.model_dump(), 'id': new_id}


@app.put("/items/{item_id}")
async def update_item(item_id: int, new_item: ItemIn):
    query = items_db.update().where(items_db.c.id == item_id).values(**new_item.model_dupm())
    await database.execute(query)
    return {'message': 'item updated'}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items_db.delete().where(items_db.c.id == item_id)
    await database.execute(query)
    return {'massage': 'item deleted'}

@app.get("/orders/", response_model=List[Order])
async def read_orders():
    query = orders_db.select()
    return await database.fetch_all(query)

@app.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders_db.select().where(orders_db.c.id == order_id)
    return await database.fetch_one(query)


@app.post("/orders/", response_model=Order)
async def create_order(order: OrderIn):
    new_order = orders_db.insert().values(**order.model_dump())
    new_id = await database.execute(new_order)
    return {**order.model_dump(), 'id': new_id}

@app.put("/orders/{order_id}")
async def update_order(order_id: int, new_order: OrderIn):
    query = orders_db.update().where(orders_db.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {'message': 'Order updated'}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders_db.delete().where(orders_db.c.id == order_id)
    await database.execute(query)
    return {'message': 'order deleted'}

