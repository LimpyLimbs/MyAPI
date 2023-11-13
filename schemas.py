from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, conint, conlist

class Dish(Enum):
    burito = 'burito'
    burito_bowl = 'burrito_bowl'
    tacos = 'tacos'

class Meat(Enum):
    chicken = 'chicken'
    steak = 'steak'
    barbacoa = 'barbacoa'

class Toppings(Enum):
    beans = 'beans'
    rice = 'rice'
    salsa = 'salsa'
    sour_cream = 'sour_cream'
    cheese = 'cheese'
    corn = 'corn'
    guacamole = 'guacamole'

class OrderItemSchema(BaseModel):
    dish: Dish
    meat: Meat
    toppings: Optional[Toppings]
    # I think it needs to be toppings: List[Optional[Toppings]]
