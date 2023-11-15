from enum import Enum
from typing import Optional, Union, List
from uuid import UUID
from pydantic import BaseModel, conint, conset # , Field, conlist, 

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
    
# appetizer definitions

class Appetizer(Enum):
    chips ='chips'
    queso = 'queso'
    salsa = 'salsa'
    guacamole = 'guacamole'
    
# order definitions
    
class Entree(BaseModel):
    entree_type: EntreeType
    meat: Meat
    toppings: conset(Optional[Toppings])

class Drink(BaseModel):
    size: Size
    liquid: Liquid

class OrderItemSchema(BaseModel):
     item: Union[Appetizer, Drink, Entree]
     quantity: Optional[conint(ge=1, strict=True)] = 1
     
class CreateOrderSchema(BaseModel):
    order: List[OrderItemSchema]
