from q_pos.business import schema as business_schema
import graphene
from graphene_django.debug import DjangoDebug


class Query(business_schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


class RootMutation(business_schema.BusinessMutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="__debug")


schema = graphene.Schema(query=Query, mutation=RootMutation)
