from django.conf.urls import url

from rest_framework import routers

from .card_api import CardViewSet
from .collection_api import CollectionViewSet
from .user_api import UserCreateView

router = routers.DefaultRouter()
router.register(r'card', CardViewSet)
router.register(r'collection', CollectionViewSet, 'collection')
urlpatterns = router.urls


urlpatterns += [
    url(r'^user$', UserCreateView.as_view())
]
