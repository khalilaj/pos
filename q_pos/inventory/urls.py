from django.conf.urls import url
from .views import InventoryListCreate, InventoryRetrieveUpdate
urlpatterns = [    
    url(r'^$', InventoryListCreate.as_view(), name='list-create-inventory'),
    url(r'^(?P<pk>\d+)$', InventoryRetrieveUpdate.as_view(), name='retrieve-inventory'),
]