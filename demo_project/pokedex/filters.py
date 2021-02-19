import django_filters
from django_filters.rest_framework import FilterSet

from pokedex.models import Pokemon


class PokemonFilter(FilterSet):
    specie__identifier = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Pokemon
        fields = ('id', 'identifier', 'specie__identifier', 'specie__generation',
                  'specie', 'height', 'weight', 'base_experience', 'is_default')
