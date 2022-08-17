from functools import wraps
from fastapi import  status
from fastapi import Response

def only_product_owner():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            response = kwargs.get('response')
            user = kwargs.get('user')
            for i in user.group: 
                if i.name != 'Product-Owner':
                    response.status_code = status.HTTP_403_FORBIDDEN
                    return {'error':'Only product owner can do this operation!'}
            return  f(*args, **kwargs)
        return decorated_function
    return decorator
    
def only_customer():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            response = kwargs.get('response')
            user = kwargs.get('user')
            for i in user.group: 
                if i.name != 'Customer':
                    response.status_code = status.HTTP_403_FORBIDDEN
                    return {'error':'Only customer can do this operation!'}
            return  f(*args, **kwargs)
        return decorated_function
    return decorator
