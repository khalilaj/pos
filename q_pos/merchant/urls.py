from django.conf.urls import url
from .views import MerchantListCreate, MerchantRetrieve

urlpatterns = [
    url(r'^$', MerchantListCreate.as_view(), name='list-create-merchant'),
    url(r'^(?P<pk>\d+)$', MerchantRetrieve.as_view(), name='retrieve-merchant'),
]
