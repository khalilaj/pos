from django.conf.urls import url
from .views import PaymentMethodListCreate, PaymentMethodRetrieve

urlpatterns = [
    url(r'^$', PaymentMethodListCreate.as_view(), name='list-create-payment-method'),
    url(r'^(?P<pk>\d+)$', PaymentMethodRetrieve.as_view(), name='retrieve-update-payment-method'),
]
