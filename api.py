import uuid
from datetime import datetime
from app import app
from starlette.responses import Response
from starlette import status
from schemas import OrderItemSchema, CreateOrderSchema, GetOrderSchema

ORDERS = []

@app.get('/orders')
def get_orders():
    return ORDERS

@app.post('/orders/', 
          status_code=status.HTTP_201_CREATED,
          response_model=GetOrderSchema,
)
def create_order(order_details: CreateOrderSchema):
    order = order_details.dict()
    order['uuid'] = uuid.uuid4()
    order['created'] = datetime.utcnow()
    order['status'] = 'created'
    ORDERS.append(order)
    return order
