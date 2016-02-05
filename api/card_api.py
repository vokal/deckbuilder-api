from rest_framework import viewsets

from card.serializers import CardSerializer
from card.models import Card


class CardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
