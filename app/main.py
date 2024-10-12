from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler
from graphene import Schema
from app.gql.queries import Query
from app.db.database import prepare_database, Session
from app.db.models import Employer, Job

schema = Schema(query=Query)

app = FastAPI()


@app.on_event("startup")
def startup_event():
    print("I m called ")
    prepare_database()


@app.get("/employers")
def get_employers():
    with Session() as session:
        employers = session.query(Employer).all()
        return employers


@app.get("/jobs")
def get_jobs():
    with Session() as session:
        jobs = session.query(Job).all()
        return jobs


app.mount("/graphql", GraphQLApp(
    schema=schema,
    on_get=make_playground_handler()
))
