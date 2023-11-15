from enum import Enum
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, conint, conlist, conset

# drink definitions

class Liquid(Enum):
    water = 'water'
    juice = 'juice'
    soda = 'soda'

class Size(Enum):
    small = 'small'
    medium = 'medium'
    large = 'large'
    
# entree definitions

class EntreeType(Enum):
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

class Appetizer(Enum):
    chips ='chips'
    queso = 'queso'
    salsa = 'salsa'
    guacamole = 'guacamole'
    
class OrderEntreeSchema(BaseModel):
    entree_type: EntreeType
    meat: Meat
    toppings: conset(Optional[Toppings])

class OrderDrinkSchema(BaseModel):
    size: Size
    liquid: Liquid  
    
class OrderItemSchema(BaseModel):
    entree: OrderEntreeSchema
    drink: OrderDrinkSchema
    appetizer: Appetizer
    quantity: Optional[conint(ge=1, strict=True)] = 1
