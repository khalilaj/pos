from django.conf.urls import url
from .views import CustomerListCreate, CustomerRetrieve

urlpatterns = [
    url(r'^$', CustomerListCreate.as_view(), name='list-create-customer'),
    url(r'^(?P<pk>\d+)$', CustomerRetrieve.as_view(), name='retrieve-update-customer'),
]
