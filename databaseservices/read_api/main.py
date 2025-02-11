from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "dbname=mydatabase user=user password=password host=db")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.get("/read/")
def read_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    return {"data": data}
