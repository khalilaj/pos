from django.core.cache import cache

import graphene
from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType
from q_pos.business.models import Business
from q_pos.core.graph import RelayNode


class BusinessNode(DjangoObjectType):
    class Meta:
        model = Business
        interfaces = (RelayNode,)


class BusinessConnection(relay.Connection):
    class Meta:
        node = BusinessNode


class Query(graphene.ObjectType):

    business = graphene.Field(BusinessNode, id=graphene.Int())

    all_businesses = relay.ConnectionField(BusinessConnection)

    def resolve_business(self, info, **kwargs):
        return Business.objects.get(pk=kwargs.get("id"))

    def resolve_all_businesses(self, info, **kwargs):
        return Business.objects.all()
