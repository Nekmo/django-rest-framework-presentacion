from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from pokedex.filters import PokemonFilter, SpecieFilter, RegionFilter, GenerationFilter, HabitatFilter, ShapeFilter, \
    GrowthRateFilter
from pokedex.models import Pokemon, Specie, GrowthRate, Generation, Habitat, Shape, Region
from pokedex.serializers import PokemonSerializer, SpecieSerializer, GrowthRateSerializer, \
    ShapeSerializer, HabitatSerializer, GenerationSerializer, RegionSerializer, DetailPokemonSerializer

PHOTO_FORMAT_URL = 'https://img.pokemondb.net/artwork/{identifier}.jpg'


class SpecieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
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

    Additionally we also provide an extra `detail_list` and `photo` actions.
    """
    queryset = Pokemon.objects.select_related('specie')
    serializer_class = PokemonSerializer
    filter_class = PokemonFilter
    ordering_fields = ('id', 'identifier', 'specie__generation__identifier', 'height',
                       'weight', 'base_experience', 'order', 'is_default')
    search_fields = ('identifier',)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'detail_list']:
            return DetailPokemonSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ['retrieve', 'detail_list']:
            queryset = queryset.select_related('specie__growth_rate', 'specie__shape', 'specie__habitat',
                                               'specie__generation')
        return queryset

    @action(detail=False)
    def detail_list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(detail=True)
    def photo(self, *args, **kwargs):
        obj = self.get_object()
        photo_url = PHOTO_FORMAT_URL.format(**vars(obj))
        return Response(headers={'Location': photo_url}, status=status.HTTP_302_FOUND)
