import fastapi
import uvicorn

from views import home
from api import weather_api

import os

# os.chdir(os.getcwd())

api = fastapi.FastAPI()


###################################################################
### Call Routers
###################################################################

# 1. As simple Calls
# api.include_router(home.router)
# api.include_router(weather_api.router)

# 2. As function
def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)

configure()

###################################################################

if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)