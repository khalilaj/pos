from django.conf.urls import url
from .views import CategoryListCreate, CategoryRetrieve

urlpatterns = [
    url(r"^$", CategoryListCreate.as_view(), name="list-create-category"),
    url(r"^(?P<pk>\d+)$", CategoryRetrieve.as_view(), name="retrieve-update-category"),
]
