from fastapi import APIRouter
from app.services.job_service import JobsService

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

service = JobsService()

@router.get("/sync")
def sync_jobs():
    jobs = service.fetch_jobs(source=2, keyword="software engineer", country="us")
    return jobs
    # return {"code": 200, "message": "Job data synchronization started"}