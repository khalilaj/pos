from django.conf.urls import url
from .views import RoleListCreate, RoleRetrieve

urlpatterns = [
    url(r'^$', RoleListCreate.as_view(), name='list-create-role'),
    url(r'^(?P<pk>\d+)$', RoleRetrieve.as_view(), name='retrieve-update-role'),
]
