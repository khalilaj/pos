from django.core.cache import cache
from django.core.validators import validate_email

import graphene
from graphene import relay
from graphene_django import DjangoConnectionField, DjangoObjectType
from q_pos.business.models import Business
from q_pos.user.models import Account
from q_pos.core.graph import RelayNode
from q_pos.core.exceptions import ResourceDoesNotExist
from graphene_django.rest_framework.mutation import SerializerMutation
from q_pos.core.models import get_or_raise


class BusinessNode(DjangoObjectType):
    class Meta:
        model = Business
        interfaces = (RelayNode,)


class BusinessConnection(relay.Connection):
    class Meta:
        node = BusinessNode


# Fetching data
class Query(graphene.ObjectType):
    business = graphene.Field(BusinessNode, id=graphene.Int())

    all_businesses = relay.ConnectionField(BusinessConnection)

    def resolve_business(self, info, **kwargs):
        return Business.objects.get(pk=kwargs.get("id"))

    def resolve_all_businesses(self, info, **kwargs):
        return Business.objects.all()


class CreateBusiness(graphene.Mutation):
    """
    TODO 
    Should probably use Graphene Rest Framework mutation
        https://docs.graphene-python.org/projects/django/en/latest/rest-framework/#mutation
    Use relay.ClientIDMutation when using relay lib on client
        https://github.com/graphql-python/graphene/issues/659#issuecomment-400960904
    """

    class Input:
        account_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        nickname = graphene.String()
        location = graphene.String()
        logo = graphene.String()

    business = graphene.Field(BusinessNode)

    def mutate(cls, info, account_id, name, email, nickname, location, logo):

        validate_email(email)
        account = get_or_raise(Account, pk=account_id, error_msg="Account with id {} does not exist".format(account_id))

        business = Business.objects.create(
            merchant=account,
            name=name,
            email=email,
            nickname=nickname,
            location=location,
            logo=logo,
        )
        return CreateBusiness(business=business)


class BusinessMutation(graphene.ObjectType):
    """
    mutation CreateBusiness{
        createBusiness(accountId: 2000, email:"mail@fgexample.com", phone_number: "07655678765", location:"" , logo:"",  name:"jh", nickname:"jhg"){
            business{
            name
            }
        }
    }
    """

    create_business = CreateBusiness.Field()
