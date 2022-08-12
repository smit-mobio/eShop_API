from functools import wraps
from fastapi import  status

def only_product_owner(func):
    @wraps(func)
    def decorated_function(response,user, *args, **kwargs ):
        for i in user.group: 
            if i.name != 'Product-Owner':
                response.status_code = status.HTTP_403_FORBIDDEN
                return {'error':'Only product owner can do this operation!'}
        return  func(response, user, *args, **kwargs)
    return decorated_function
    
