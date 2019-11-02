from django.conf.urls import url
from custom_profile import views
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    url(r'^signin/$', drf_views.obtain_auth_token, name='auth'),
    url(r'^signup/$', views.sign_up),
    url(r'^$', views.ProfileAPIView.as_view())
]