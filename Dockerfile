FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# PWD: /app
EXPOSE 80
ARG app=app_1_calculator

RUN echo $app
COPY /$app /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "80"]


# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
# # PWD: /app
# EXPOSE 80

# COPY . /app
# RUN pip install -r requirements.txt
# CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "80"]