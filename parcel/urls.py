from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from parcel import views



urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.ParcelDetailUpdateAPIView.as_view()),
    url(r'^$', views.ParcelListCreateAPIView.as_view()),
]