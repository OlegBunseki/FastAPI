import fastapi
from fastapi.applications import FastAPI
from requests.api import request
import uvicorn

import threading
import time

api = FastAPI()
lock = threading.Lock()


#####################################################################

@api.get('/', include_in_schema=False)
def index():
    return {'key': 'value'}

#####################################################################

@api.get('/run')
def run_code(a: int, b: int):
    time.sleep(5)
    return {'result': a + b}

#####################################################################

@api.get('/run1')
def run_one():
    time.sleep(10)
    return {'status': 'ok'}


@api.get('/run2')
def run_one():
    return {'status': 'ok'}

#####################################################################

@api.get('/info')
def get_status():

    if lock.locked():
        return {'status': 'not available'}
    else:
        return {'status': 'available'}   


@api.get('/run_lock')
def run_code(a: int, b: int, i: int):

    if lock.locked():
        return get_status()
        
    else:
        lock.acquire()
        print(i, lock.locked())

        # MY CODE HERE #####################
        
        time.sleep(10)
        
        ####################################

        lock.release()
        print(i, lock.locked())

        return {'result': a + b}


uvicorn.run(api, host='127.0.0.1', port=8000)