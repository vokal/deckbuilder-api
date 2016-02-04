from django.db import models
from django.conf import settings


class Card(models.Model):

    heros = ['druid', 'hunter', 'mage',
             'paladin', 'priest', 'rogue',
             'shaman', 'warlock', 'warrior', 'neutral']
    card_types = ['minion', 'spell', 'weapon']
    card_sets = ['basic', 'classic', 'reward', 'naxx', 'gvg', 'brm', 'tgt', 'loe']
    rarities = ['free', 'common', 'rare', 'epic', 'legendary']
    tribes = ['beast', 'demon', 'dragon', 'mech', 'murloc', 'pirate', 'totem']

    name = models.CharField(max_length=50)
    mana = models.SmallIntegerField()
    hero = models.CharField(max_length=16, choices=[(i, i) for i in heros])
    card_type = models.CharField(max_length=16, choices=[(i, i) for i in card_types])
    card_set = models.CharField(max_length=16, choices=[(i, i) for i in card_sets])
    rarity = models.CharField(max_length=16, choices=[(i, i) for i in rarities])
    text = models.TextField(blank=True)
    tribe = models.CharField(null=True, max_length=16, choices=[(i, i) for i in tribes])
    attack = models.SmallIntegerField(null=True)
    health = models.SmallIntegerField(null=True)

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Collection',
                                   related_name='collection')

    def __str__(self):
        return self.name


class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    card = models.ForeignKey(Card)

    count = models.SmallIntegerField()
