from django.conf.urls import url
from .views import BusinessListCreate, BusinessRetrieveUpdateDestroy

urlpatterns = [    
    url(r'^$', BusinessListCreate.as_view(), name='list-create-business'),
    url(r'^(?P<pk>\d+)$', BusinessRetrieveUpdateDestroy.as_view(), name='retrieve-business'),
]