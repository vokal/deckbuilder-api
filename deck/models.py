from django.db import models


class Deck(models.Model):
    heros = ['druid', 'hunter', 'mage',
             'paladin', 'priest', 'rogue',
             'shaman', 'warlock', 'warrior']
    name = models.CharField(max_length=32)
    hero = models.CharField(max_length=16, choices=[(i, i) for i in heros])

    cards = models.ManyToManyField("card.Card", through="CardInDeck",
                                   related_name="decks_in")


class CardInDeck(models.Model):
    deck = models.ForeignKey(Deck)
    card = models.ForeignKey("card.Card")

    count = models.SmallIntegerField()

    class Meta:
        unique_together = ('deck', 'card')
