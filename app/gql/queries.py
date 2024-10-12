from graphene import ObjectType, List
from sqlalchemy.orm import joinedload
from app.db.database import Session
from app.gql.types import EmployerObject, JobObject
from app.db.models import Employer,Job


class Query(ObjectType):
    jobs = List(JobObject)
    employers = List(EmployerObject)

    @staticmethod
    def resolve_jobs(root, info):
        with Session() as session:
            return session.query(Job).options(joinedload(Job.employer)).all()

    @staticmethod
    def resolve_employers(root, info):
        with Session() as session:
            return session.query(Employer).options(joinedload(Employer.jobs)).all()
