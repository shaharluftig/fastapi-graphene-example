import graphene
import uvicorn
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler

from config import config
from graphql.queries.query import Query

app = FastAPI()


@app.get("/")
def is_alive():
    return {"Is_alive": True}


app.add_route(config.graphql_route, GraphQLApp(schema=graphene.Schema(query=Query), on_get=make_playground_handler()))

if __name__ == '__main__':
    uvicorn.run(app, host=config.host, port=config.port)
