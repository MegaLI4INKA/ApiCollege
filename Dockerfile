FROM python:3.10

WORKDIR /ApiCollege

COPY . .

RUN pip install mysqlclient mysqlclient fastapi pyodbc sqlalchemy uvicorn mysqlx pydantic requests

EXPOSE 8000

CMD ["uvicorn","src.college.app:app", "--host", "0.0.0.0", "--port", "8000"]