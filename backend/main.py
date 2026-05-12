from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from workflow import Workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

workflow = Workflow()


class TaskRequest(BaseModel):
    task: str


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/run")
def run_task(req: TaskRequest):

    return workflow.run(req.task)
