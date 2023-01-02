import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from starlette.applications import Starlette
from .mututations import Query, Mutation, Subscription
from .mututations import router


def CreateAPP():
    app = FastAPI()
    app.include_router(router)
    app.mount("/", GraphQLApp(schema=graphene.Schema(Query, Mutation, Subscription),
              on_get=make_graphiql_handler()))
    return app


app = CreateAPP()
