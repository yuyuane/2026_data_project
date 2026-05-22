# define the model for the jobs table
from pydantic import BaseModel, Field

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, TIMESTAMP, BigInteger, SmallInteger, func
from sqlalchemy.ext.declarative import declarative_base

from app.database.database import Base

class JobsModel(Base):
    __tablename__ = "jobs"

    id = Column(BigInteger, primary_key=True, index=True)
    job_uid = Column(String(255), unique=True, nullable=False)
    name = Column(String(500), nullable=False)
    publish_time = Column(TIMESTAMP)
    company = Column(String(255))
    company_detail = Column(Text)
    followers = Column(Integer, default=0)
    apply_type = Column(SmallInteger, default=1)
    employment_type = Column(SmallInteger, default=1)
    work_mode = Column(SmallInteger, default=1)
    work_place = Column(String(255))
    applicants = Column(Integer, default=0)
    detail = Column(Text)
    source = Column(SmallInteger, nullable=False)
    source_url = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )