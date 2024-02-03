from pydantic import BaseModel, Field
from typing import List
from datetime import date

class TaskIn(BaseModel):
    title: str = Field(title="title", max_length=50)
    description: str = Field(title="Description", max_length=150)
    done: bool = Field(title="Done", default=False)


class TaskOut(TaskIn):
    id: int


class ItemIn(BaseModel):
    name: str = Field(title="Name", max_length=100)
    description: str = Field(title="Description", max_length=250)
    price: float = Field(title="Price", default=0.0, gt=0, le=100000)


class Item(ItemIn):
    id: int


class UserIn(BaseModel):
    username: str = Field(title="Username", max_length=50)
    lastname: str = Field(title="Lastname", max_length=50)
    email: str = Field(title="Email", max_length=128)
    password: str = Field(title="Password", max_length=128)


class User(UserIn):
    id: int


class OrderIn(BaseModel):
    user_id: int
    item_id: int
    date: date
    done: bool = Field(title="Done", default=False)


class Order(OrderIn):
    id: int