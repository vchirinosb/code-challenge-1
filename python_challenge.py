"""
Refactor the next function using yield to return the array of objects found by the
`s3.list_objects_v2` function that matches the given prefix.
"""
def get_s3_objects(bucket, prefix=''):
    s3 = boto3.client('s3')

    kwargs = {'Bucket': bucket}
    next_token = None
    if prefix:
        kwargs['Prefix'] = prefix
    object_list = []
    while True:
        if next_token:
            kwargs['ContinuationToken'] = next_token
        resp = s3.list_objects_v2(**kwargs)
        contents = resp.get('Contents', [])
        for obj in contents:
            key = obj['Key']
            if key.startswith(prefix):
                object_list.append(obj)
        next_token = resp.get('NextContinuationToken', None)

        if not next_token:
            break
    return object_list

"""
Please, full explain this function: document iterations, conditionals, and the
function as a whole
"""
def fn(main_plan, obj, extensions=[]):
    
    items = []
    sp = False
    cd = False

    ext_p = {}

    for ext in extensions:
        ext_p[ext['price'].id] = ext['qty']

    for item in obj['items'].data:
        product = {
            'id': item.id
        }

        if item.price.id != main_plan.id and item.price.id not in ext_p:
            product['deleted'] = True
            cd = True
        elif item.price.id in ext_p:
            qty = ext_p[item.price.id]
            if qty < 1:
                product['deleted'] = True
            else:
                product['qty'] = qty
            del ext_p[item.price.id]
        elif item.price.id == main_plan.id:
            sp = True


        items.append(product)
    
    if not sp:
        items.append({
            'id': main_plan.id,
            'qty': 1
        })
    
    for price, qty in ext_p.items():
        if qty < 1:
            continue
        items.append({
            'id': price,
            'qty': qty
        })
    
    return items


"""
Having the class `Caller` and the function `fn`
Refactor the function `fn` to execute any method from `Caller` using the argument `fn_to_call`
reducing the `fn` function to only one line.
"""
class Caller:
    add = lambda a, b : a + b
    concat = lambda a, b : f'{a},{b}'
    divide = lambda a, b : a / b
    multiply = lambda a, b : a * b

def fn(fn_to_call, *args):
    result = None

    if fn_to_call == 'add':
        result = Caller.add(*args)
    if fn_to_call == 'concat':
        result = Caller.concat(*args)
    if fn_to_call == 'divide':
        result = Caller.divide(*args)
    if fn_to_call == 'multiply':
        result = Caller.multiply(*args)

    return result


"""
A video transcoder was implemented with different presets to process different videos in the application. The videos should be
encoded with a given configuration done by this function. Can you explain what this function is detecting from the params
and returning based in its conditionals?
"""
def fn(config, w, h):
    v = None
    ar = w / h

    if ar < 1:
        v = [r for r in config['p'] if r['width'] <= w]
    elif ar > 4 / 3:
        v = [r for r in config['l'] if r['width'] <= w]
    else:
        v = [r for r in config['s'] if r['width'] <= w]

    return v

"""
Having the next helper, please implement a refactor to perform the API call using one method instead of rewriting the code
in the other methods.
"""
import requests
class Helper:
    DOMAIN = 'http://example.com'
    SEARCH_IMAGES_ENDPOINT = 'search/images'
    GET_IMAGE_ENDPOINT = 'image'
    DOWNLOAD_IMAGE_ENDPOINT = 'downloads/images'

    AUTHORIZATION_TOKEN = {
        'access_token': None,
        'token_type': None,
        'expires_in': 0,
        'refresh_token': None
    }

        
    def search_images(self, **kwargs):
        token_type = self.AUTHORIZATION_TOKEN['token_type']
        access_token = self.AUTHORIZATION_TOKEN['access_token']

        headers = {
            'Authorization': f'{token_type} {access_token}',
        }

        URL = f'{self.DOMAIN}/{self.SEARCH_IMAGES_ENDPOINT}'

        send = {
            'headers': headers,
            'params': kwargs
        }

        response = request.get(requests, method)(URL, **send)
        return response
        
    def get_image(self, image_id, **kwargs):
        token_type = self.AUTHORIZATION_TOKEN['token_type']
        access_token = self.AUTHORIZATION_TOKEN['access_token']

        headers = {
            'Authorization': f'{token_type} {access_token}',
        }

        URL = f'{self.DOMAIN}/{self.GET_IMAGE_ENDPOINT}/{image_id}'

        send = {
            'headers': headers,
            'params': kwargs
        }

        response = request.get(requests, method)(URL, **send)
        return response

    def download_image(self, image_id, **kwargs):
        token_type = self.AUTHORIZATION_TOKEN['token_type']
        access_token = self.AUTHORIZATION_TOKEN['access_token']

        headers = {
            'Authorization': f'{token_type} {access_token}',
        }

        URL = f'{self.DOMAIN}/{self.DOWNLOAD_IMAGE_ENDPOINT}/{image_id}'

        send = {
            'headers': headers,
            'data': kwargs
        }

        response = request.post(requests, method)(URL, **send)
        return response
