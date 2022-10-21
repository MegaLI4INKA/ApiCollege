FROM python:3.10

WORKDIR /PetProdjectFastApi

COPY . .

RUN pip install fastapi
RUN pip install sqlalchemy
RUN pip install uvicorn
RUN pip install mysqlx
RUN pip install pydantic
RUN pip install fastapi
RUN pip install pyodbc

EXPOSE 8000

CMD ["python","__main__.py"]