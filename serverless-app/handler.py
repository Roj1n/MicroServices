from order_service import app as order_app
from product_service import app as product_app
from user_service import app as user_app
from serverless_wsgi import handle_request
import json

def order(event, context):
    response = handle_request(order_app, event, context)
    response['body'] = json.dumps({'message': 'Order service in serverless is running successfully'})
    return response

def product(event, context):
    response = handle_request(product_app, event, context)
    response['body'] = json.dumps({'message': 'Product service in serverless is running successfully'})
    return response

def user(event, context):
    response = handle_request(user_app, event, context)
    response['body'] = json.dumps({'message': 'User service in serverless is running successfully'})
    return response
