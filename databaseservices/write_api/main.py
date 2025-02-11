from fastapi import FastAPI, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL", "dbname=mydatabase user=user password=password host=db")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)

@app.post("/write/")
def write_data(username: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    
    if not user:
        raise HTTPException(status_code=403, detail="Vous ne pouvez qu'accéder en lecture")
    
    cursor.execute("INSERT INTO data (username, message) VALUES (%s, %s)", (username, "Hello World!"))
    conn.commit()
    
    return {"message": "Donnée ajoutée avec succès"}
