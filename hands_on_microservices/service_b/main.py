from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/data")
async def get_data():
    return {"message": "Hello from Service B!"}

if __name__ == "__main__":
    uvicorn.run(app, uds="/tmp/service_b.sock")
