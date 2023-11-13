from uuid import UUID
from datetime import datetime
from app import app
from starlette.responses import Response
from starlette import status
from schemas import OrderItemSchema

orders = []

@app.get('/orders')
def get_orders():
    return orders

@app.post('/orders/', status_code=status.HTTP_201_CREATED)
def create_order(order_details: OrderItemSchema):
    # order = order_details.dict()
    return orders
