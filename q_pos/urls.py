from django.conf.urls import include,url
from .user import views

urlpatterns = [
    url(r'^login/', views.LoginView.as_view()),
    url(r'^register/', views.RegistrationView.as_view()),
    url(r'^user/', include('q_pos.user.urls')),
    url(r'^business/', include('q_pos.business.urls')),
    url(r'^category/', include('q_pos.category.urls')),
    url(r'^product/', include('q_pos.product.urls')),
    url(r'^sale/', include('q_pos.sale.urls')),
    url(r'^payment_method/', include('q_pos.payment_method.urls')),
]
