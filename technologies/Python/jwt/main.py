from fastapi import FastAPI
import uvicorn

app = FastAPI(title="JWT FastAPI Tutorial")

@app.get("/")
def read_root():
    return {"message": "JWT Server is running!"}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, port=8001)