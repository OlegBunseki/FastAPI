# Helpful Links:
- pydantic: https://pydantic-docs.helpmanual.io/
- fastapi: https://fastapi.tiangolo.com/
- starlette: https://www.starlette.io/


# YouTube Videos:
- Webinar with Michael Kennedy: https://www.youtube.com/watch?v=sBVb4IB3O_U


# General Structure:
The HTTP verbs comprise a major portion of our “uniform interface” constraint and provide us the action counterpart to the noun-based resource. 
The primary or most-commonly-used HTTP verbs (or methods, as they are properly called) are:
1. POST
2. GET
3. PUT
4. PATCH
5. DELETE 


# JSON Schemas / working with json
- https://json-schema.org/
- https://realpython.com/python-json/


# Python Types
- Intro: https://fastapi.tiangolo.com/python-types/
- Docs: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

# GET vs. POST (die beiden wichtigsten HTTP-Requests im Vergleich)
- https://www.ionos.de/digitalguide/websites/web-entwicklung/get-vs-post/
- https://www.w3schools.com/tags/ref_httpmethods.asp


# Concurrency and async / await
- https://fastapi.tiangolo.com/async/#in-a-hurry


# enum
- https://www.tutorialspoint.com/enum-in-python
- https://florian-dahlitz.de/blog/why-you-should-use-more-enums-in-python



# Deploy to Azure App Service
1. Create App Service
2. Go to Deployment Center: Connect to GitHub Account and select branch from where to deploy
3. Got To Configuration: General Settings: Select Startup Command

For FastAPI:
- add uvicorn to requirements.txt
- start.sh = python -m uvicorn main:api --host 0.0.0.0 