import fastapi
import uvicorn

api = fastapi.FastAPI()

# To run in dev view
# uvicorn calculate_api:api --reload


@api.get('/whatistheanswer')
def answer():
    return {'answer': 42}


@api.get('/api/{item}')
def item_value(item: int):
    return {'key': item}


@api.get('/calculator')
def calcualte(a: int, b: int, function: str):
    return {'result': eval(f'({a}).__{function}__({b})')}



### VERSION 1
# uvicorn app_1_calculator.main:api --reload

### VERSION 2
if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)


