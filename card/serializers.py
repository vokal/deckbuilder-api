from rest_framework import serializers

from .models import Card, Collection


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ('users', )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('card', 'count')
        depth = 1

    def to_representation(self, obj):
        res = super(CollectionSerializer, self).to_representation(obj)
        card = res.pop('card')
        res.update(card)
        return res



class CollectionAddRemoveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count = serializers.IntegerField()
