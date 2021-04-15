from models.location import Location
import httpx

async def get_live_data(location: Location):

    url = f"https://weather.talkpython.fm/api/weather?city={location.city}&counry={location.country}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    data = response.json()

    # something not found: {'cod': '404', 'message': 'city not found'}
    
    return data