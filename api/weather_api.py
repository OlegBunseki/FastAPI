import fastapi 
from fastapi import HTTPException
from typing import Optional
import requests

# MODELS
from models.location import Location
from models.nested import LocationNested
from models.nested import Coordinates
from models.nested import LocationOptional
from models.umbrella_status import UmbrellaStatus

# SERVICES
from services import live_weather_service


router = fastapi.APIRouter()


#####################################################################
### Parameters (Simple / BaseModel)
#####################################################################

@router.get('/api/umbrella_v1.1')
def do_i_need_umbrella(city: str, country: str='us', state: Optional[str]=None):
    return {'city': city}


@router.get('/api/umbrella_v1.2')
def do_i_need_umbrella(location: Location):
    return location

# The request comes in the BODY!
# Therefore it needs a POST and not a GET request

@router.post('/api/umbrella_v1.3')
def do_i_need_umbrella(location: Location):
    return location


#####################################################################
### fastapi.Depends() -> Solves the GET vs. POST from above
#####################################################################

@router.get('/api/umbrella_v2.1')
def do_i_need_umbrella(location: Location = fastapi.Depends()):
    return location


@router.get('/api/umbrella_v2.2')
def do_i_need_umbrella(location: Location = fastapi.Depends()):

    print(location.city)
    # print(location['city']) -> TypeError: 'Location' object is not subscriptable

    loc = location.dict()
    print(loc['city'])

    return loc


#####################################################################
### Response Model
#####################################################################

@router.get('/api/umbrella_v3.1', response_model=UmbrellaStatus)
def do_i_need_umbrella(location: Location = fastapi.Depends()):
    return 1 # Internal Server Error


@router.get('/api/umbrella_v3.2', response_model=UmbrellaStatus)
def do_i_need_umbrella(location: Location = fastapi.Depends()):
    
    output = UmbrellaStatus(weather_category='unknown',
                            bring_umbrella=False,
                            temp=0.0)
    
    return output


@router.get('/api/umbrella_v3.3', response_model=UmbrellaStatus)
def do_i_need_umbrella(location: Location = fastapi.Depends()):

    url = f"https://weather.talkpython.fm/api/weather?city={location.city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    forecast = data.get('forecast', {})
    temp = forecast.get('temp', {})


    umbrella = UmbrellaStatus(bring_umbrella=False, temp=temp, weather_category='unknown')
        
    return umbrella


#####################################################################
### aync / wait
#####################################################################

@router.get('/api/umbrella_v4.1', response_model=UmbrellaStatus)
async def do_i_need_umbrella(location: Location = fastapi.Depends()):

    data = await live_weather_service.get_live_data(location)

    weather = data.get('weather', {})
    category = weather.get('category', 'unknown')

    forecast = data.get('forecast', {})
    temp = forecast.get('temp', -100)

    bring = category.lower() == 'clouds'
    

    umbrella = UmbrellaStatus(weather_category=category, bring_umbrella=bring, temp=temp)
        
    return umbrella


#####################################################################
### Nested BaseModel
#####################################################################

@router.get('/api/umbrella_v5.1', response_model=LocationNested)
def do_i_need_umbrella():

    coordinates = Coordinates(x=5.5, y=6.6)
    output = LocationNested(city='Berlin', country='Germany', coordinates=coordinates)

    return output


#####################################################################
### Reponse: Optional Arguments
#####################################################################

@router.get('/api/umbrella_v6.1', response_model=LocationOptional)
def do_i_need_umbrella(loc: LocationOptional = fastapi.Depends()):
    
    output = LocationOptional(city='berlin', country='germany')
    
    return output


@router.get('/api/umbrella_v6.2', response_model=LocationOptional, response_model_exclude_unset=True)
def do_i_need_umbrella(loc: LocationOptional = fastapi.Depends()):
    
    output = LocationOptional(city='berlin', country='germany')
    
    return output


@router.post('/api/umbrella_v6.3', response_model=LocationOptional, response_model_exclude_unset=True)
def do_i_need_umbrella(loc: LocationOptional = fastapi.Depends()):
    
    output = LocationOptional(city='berlin', country='germany')
    
    return output


#####################################################################
### HTTPException
#####################################################################

@router.post('/api/umbrella_v7.1', response_model=LocationOptional, response_model_exclude_unset=True)
def do_i_need_umbrella(loc: LocationOptional = fastapi.Depends()):
    
    if 1 != 2:
        raise HTTPException(status_code=404, detail="Item not found")

    output = LocationOptional(city='berlin', country='germany')
    
    return output

