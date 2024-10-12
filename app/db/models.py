from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String as saString, ForeignKey

from sqlalchemy.orm import relationship

Base = declarative_base()


class Employer(Base):
    __tablename__ = "employers"
    id = Column(Integer, primary_key=True)
    name = Column(saString)
    contact_email = Column(saString)
    industry = Column(saString)
    jobs = relationship("Job", back_populates="employer")


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    title = Column(saString)
    description = Column(saString)
    employer_id = Column(Integer, ForeignKey("employers.id"))
    employer = relationship("Employer", back_populates="jobs")
