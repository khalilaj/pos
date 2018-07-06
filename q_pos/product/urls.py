from django.conf.urls import url
from .views import ProductListCreate, ProductRetrieve


urlpatterns = [    
    url(r'^$',
        ProductListCreate.as_view(),
        name= 'list-create-product'),

    url(r'^(?P<pk>\d+)$',
        ProductRetrieve.as_view(),
        name= 'retrieve-update-product')
    ]
