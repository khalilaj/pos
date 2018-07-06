from django.conf.urls import url
from .views import EmployeeListCreate, EmployeeListCreate

urlpatterns = [
    url(r'^$', EmployeeListCreate.as_view(), name='list-create-employee'),
    url(r'^(?P<pk>\d+)$', EmployeeListCreate.as_view(), name='retrieve-tenant'),
]

