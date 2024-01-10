import uvicorn

from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import users_controller
from app.config import database

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await database.init_db()

load_dotenv()

app.include_router(users_controller.router, prefix="/api")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5000"], 
                   allow_methods=["*"], allow_headers=["*"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)