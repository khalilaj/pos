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
    all_businesses = graphene.List(BusinessNode);
    business = graphene.Field(BusinessNode, id=graphene.Int())

    all_businesses = relay.ConnectionField(BusinessConnection)

    def resolve_business(self, info, **kwargs):
        return Business.objects.get(pk=kwargs.get("id"))

    def resolve_all_businesses(self, info, **kwargs):
        return Business.objects.all()


class AddBusiness(graphene.ClientIDMutation):
    author = graphene.Field(BusinessNode)

    class Input:
        merchant = graphene.Int()
        name = graphene.String()
        nickname = graphene.String()
        email = graphene.String()
        location = graphene.String()
        logo = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        business = Business(
            merchant=input.get('merchant'),
            name=input.get('name'),
            nickname=input.get('nickname'),
            email=input.get('email'),
            location=input.get('location'),
            logo=input.get('logo'),
        )
        business.save()
        return AddBusiness(business=business)


class BusinessMutation(graphene.AbstractType):
    add_Business = AddBusiness.Field()