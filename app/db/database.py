from app.db.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings.config import DB_URL
from app.db.data import employers_data, jobs_data
from app.db.models import Employer, Job

engine = create_engine(DB_URL)
conn = engine.connect()

Session = sessionmaker(bind=engine)


def prepare_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()

    for employer in employers_data:
        emp = Employer(**employer)
        session.add(emp)

    for _job in jobs_data:
        job = Job(**_job)
        session.add(job)

    session.commit()
    session.close()
