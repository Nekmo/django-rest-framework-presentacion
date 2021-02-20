from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from pokedex.filters import PokemonFilter, SpecieFilter, RegionFilter, GenerationFilter, HabitatFilter, ShapeFilter, \
    GrowthRateFilter
from pokedex.models import Pokemon, Specie, GrowthRate, Generation, Habitat, Shape, Region
from pokedex.serializers import PokemonSerializer, UserSerializer, SpecieSerializer, GrowthRateSerializer, \
    ShapeSerializer, HabitatSerializer, GenerationSerializer, RegionSerializer


class SpecieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Specie.objects.select_related('growth_rate', 'shape', 'habitat', 'generation')
    serializer_class = SpecieSerializer
    filter_class = SpecieFilter
    ordering_fields = ('identifier', 'generation', 'evolves_from_specie', 'color', 'shape', 'habitat',
                       'gender_rate', 'capture_rate', 'base_happiness', 'is_baby', 'hatch_counter',
                       'has_gender_differences', 'growth_rate', 'forms_switchable', 'order',
                       'conquest_order')
    search_fields = ('identifier', 'generation__identifier', 'shape__identifier', 'habitat__identifier',
                     'growth_rate__identifier', 'forms_switchable')


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_class = RegionFilter
    ordering_fields = ('id', 'identifier')
    search_fields = ('identifier',)
    filter_fields = ('id', 'identifier')


class GenerationViewSet(viewsets.ModelViewSet):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer
    filter_class = GenerationFilter
    ordering_fields = ('id', 'identifier')
    search_fields = ('identifier',)
    filter_fields = ('id', 'identifier')


class HabitatViewSet(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    filter_class = HabitatFilter
    ordering_fields = ('id', 'identifier')
    search_fields = ('identifier',)
    filter_fields = ('id', 'identifier')


class ShapeViewSet(viewsets.ModelViewSet):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer
    filter_class = ShapeFilter
    ordering_fields = ('id', 'identifier')
    search_fields = ('identifier',)
    filter_fields = ('id', 'identifier')


class GrowthRateViewSet(viewsets.ModelViewSet):
    queryset = GrowthRate.objects.all()
    serializer_class = GrowthRateSerializer
    filter_class = GrowthRateFilter
    ordering_fields = ('id', 'identifier')
    search_fields = ('identifier',)
    filter_fields = ('id', 'identifier')


class PokemonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Pokemon.objects\
        .select_related('specie', 'specie__growth_rate', 'specie__shape', 'specie__habitat', 'specie__generation')
    serializer_class = PokemonSerializer
    filter_class = PokemonFilter
    ordering_fields = ('id', 'identifier', 'specie__generation__identifier', 'height',
                       'weight', 'base_experience', 'order', 'is_default')
    search_fields = ('identifier',)
