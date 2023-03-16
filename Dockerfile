FROM python:3.9
RUN pip3 install fastapi uvicorn httpx sqlalchemy psycopg2-binary==2.8.6 python-dotenv pydantic[email] passlib[bcrypt] pytest requests testfixtures
COPY ./backend /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400"]
