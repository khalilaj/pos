from django.conf.urls import include, url
from django.contrib import admin
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    url(r"^graphql/", GraphQLView.as_view(graphiql=True, schema = schema)),
    url(r"^admin/", admin.site.urls),
    url(r"^", include("q_pos.urls")),
]
