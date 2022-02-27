from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'createinsurer^$', views.UserCreate.as_view(), name='account-create'),
    url(r'getinsurer^$', views.GetUser.as_view(), name='account-get'),
]