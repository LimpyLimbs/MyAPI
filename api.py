import uuid
from uuid import UUID
from datetime import datetime
from app import app
from starlette.responses import Response
from starlette import status
from fastapi import HTTPException
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

@app.get('/orders/{order_id}',
         response_model=GetOrderSchema
)
def get_order(order_id: UUID):
    for order in ORDERS:
        if order['uuid'] == order_id:
            return order
    raise HTTPException(status_code=404, detail=f'Order {order_id} was not found')
