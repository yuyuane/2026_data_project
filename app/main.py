from fastapi import FastAPI
from app.api.job import router as job_router
app = FastAPI()

app.include_router(job_router)

@app.get("/")
def main():
    return {'code': 200, 'message': 'Hello World'}