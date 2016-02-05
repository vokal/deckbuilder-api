from rest_framework import viewsets, mixins, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from card.serializers import CollectionSerializer, CollectionAddRemoveSerializer
from card.models import Collection, Card


class CollectionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    serializer_class = CollectionSerializer

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    @list_route(methods=['put'])
    def add(self, request, *args, **kwargs):
        serializer = CollectionAddRemoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        try:
            card = Card.objects.get(id=serializer.validated_data['id'])
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            this_collection = Collection.objects.get(user=request.user,
                                                     card=card)
            this_collection.count += serializer.validated_data['count']
        except Collection.DoesNotExist:
            this_collection = Collection.objects.create(user=request.user,
                                                        card=card,
                                                        count=serializer.validated_data['count'])
        this_collection.save()
        return Response(CollectionSerializer(this_collection).data, status=status.HTTP_200_OK)

    @list_route(methods=['put'])
    def remove(self, request, *args, **kwargs):
        serializer = CollectionAddRemoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        try:
            card = Card.objects.get(id=serializer.validated_data['id'])
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            this_collection = Collection.objects.get(user=request.user,
                                                     card=card)
            if this_collection.count >= serializer.validated_data['count']:
                this_collection.count -= serializer.validated_data['count']
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Collection.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        this_collection.save()
        return Response(CollectionSerializer(this_collection).data, status=status.HTTP_200_OK)
