from django.conf.urls import url

from .user_api import UserCreateView

urlpatterns = [
    url(r'^user$', UserCreateView.as_view())
]
