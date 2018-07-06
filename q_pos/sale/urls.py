from django.conf.urls import url
from .views import SalesListCreateView, SaleRetrieveView

urlpatterns = [
    url(r'^$',
        SalesListCreateView.as_view(),
        name='list-create-sale'),

    url(r'^(?P<pk>\d+)$',
        SaleRetrieveView.as_view(),
        name='retrieve-update-delete-sale'),
]