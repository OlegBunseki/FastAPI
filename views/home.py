import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates('templates') # templates is the actual folder name!

router = fastapi.APIRouter()

@router.get('/', include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})