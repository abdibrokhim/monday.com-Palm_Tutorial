from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import palm

app = FastAPI()

origins = ['*']

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/get_response")
def get_response(prompt: str, file_name: str):
    return palm.get_response(prompt, file_name)

