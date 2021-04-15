import fastapi
import uvicorn

api = fastapi.FastAPI()

# To run in dev view
# uvicorn caclculate_api:api --reload


@api.get('/whatistheanswer')
def answer():
    return {'answer': 42}


@api.get('/calculator')
def calcualte(a: int, b: int, function: str):

    if function == 'add': 
        return {'result': a+b}
    else:
        return {}


@api.get('/api/{item}')
def item_value(item: int):

    return {'key': item}

if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)


