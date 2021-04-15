from fastapi import FastAPI
import requests
import json
import uvicorn

from typing import Optional
from pydantic import BaseModel


# Run Instruction: uvicorn cities:app --reload

app = FastAPI()

db = []

class City(BaseModel):
    city: str
    state: Optional[str] = None
    country: str


@app.get('/')
def index():
    return {'key': 'value'}


@app.get('/cities', response=City)
def get_cities():

    output = []
    
    for city in db:
        print(city)
        r = requests.get('http://worldtimeapi.org/api/timezone/{}'.format(city["timezone"]))
        if r.status_code == 200:
            result = {}
            current_time = r.json()['datetime']
            
            result['name'] = city['name']
            result['timezone'] = city['timezone']
            result['current time'] = current_time

            output.append(result)

    return output


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return db[city_id-1]


@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    print(db)
    return db[-1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}



uvicorn.run(app, host='127.0.0.1', port=8000)